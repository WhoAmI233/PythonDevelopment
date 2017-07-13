#-*- coding: utf-8 -*-
import traceback
from socket import *
from time import localtime
import time
import threading
from  multiprocessing import Pool
from multiprocessing import Process
import json

HOST=''
PORT=8888  #设置侦听端口
BUFSIZ=1024


def connectServer(client, addr):
    # 对日期进行一下格式化
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    stime = time.strftime(ISOTIMEFORMAT, localtime())
    # 设置超时时间
    client.settimeout(500)
    reConnectTimes = 0
    sumPrice = 0
    sumDate =0
    sendMessage =''

    print([stime],'连接成功,客户端地址：', addr)
    while True:
        try:
            data = client.recv(BUFSIZ)
        #超时后显示退出
        # except socket.timeout:
        #     print('time out')
        #     client.close()
        #     break
        except:
            print([stime],':other exception')
            client.close()
            break
        if not data:
            client.close()
            break
        # python3使用bytes，所以要进行编码
        # s='%s发送给我的信息是:[%s] %s' %(addr[0],ctime(), data.decode('utf8'))
        try:
            data_string = data.decode()
            if check_json_format(data_string):
                parseData = json.loads(data_string)
                for price in parseData["price"]:
                    sumPrice += int(price)
                for date in parseData["date"]:
                    sumDate += 1
                sumAverage = sumPrice/sumDate
                sendMessage='The average price of '+ str(sumDate) + ' days is:'+ str(sumAverage)
            else:
                dateIndexStart = data_string.find('Date:')+5
                dateIndexEnd = data_string.find('0:00:00')-1
                priceIndexStart = data_string.find('Price:')+6
                #priceIndexEnd = data_string.find('Price:') + 6
                sendMessage = 'The date is :' + data_string[dateIndexStart:dateIndexEnd] + ', The price is:' +data_string[priceIndexStart:]

        except:
            sendMessage =str(traceback.print_exc())
        client.send(sendMessage.encode('utf8'))
        print([stime], 'RevcMessage:', data.decode('utf8'))
    exit(0)

def check_json_format(raw_msg):
    """
    用于判断一个字符串是否符合Json格式
    :param self:
    :return:
    """
    if isinstance(raw_msg, str):       # 首先判断变量是否为字符串
        try:
            json.loads(raw_msg, encoding='UTF-8')
        except ValueError:
            #traceback.print_exc()
            return False
        return True
    else:
        return False

if __name__ == '__main__':
    # 对日期进行一下格式化
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    stime = time.strftime(ISOTIMEFORMAT, localtime())

    ADDR = (HOST, PORT)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen(5)
    pool = Pool(10)

    print([stime], '等待接入，侦听端口:%d' % (PORT))
    while True:
        tcpClientSock, address=sock.accept()
        #p = Process(target=connectServer, args=(tcpClientSock, address))
        #p.daemon = True
        #p.start()
        #p.join()
        # thread = threading.Thread(target=connectServer, args=(tcpClientSock, addr)) #多线程模式
        # thread.start()
        #t_start = time.time()
        pool.apply_async(func=connectServer, args=(tcpClientSock, address))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        #
        #t_end = time.time()
        #t = t_end - t_start
        #print('the program time is :%s' % t)

    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
    pool.terminate()
    tcpClientSock.close()
    sock.close()
