# coding:utf-8
import sys, os
from time import *

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/10/15'
#    __Desc__ = 

def getpass(prompt='', tip = 'You have typed %d characters!'):
    print prompt
    import msvcrt
    cur_character = msvcrt.getch()
    result =''+cur_character
    count = 1
    # 循环的读取从控制台输入的字符数据 get character once a time from terminal
    while cur_character!= '\r':
        sys.stdout.write(tip%(count)+"\r")
        sys.stdout.flush()
        cur_character = msvcrt.getch()
        result += cur_character
        count += 1
    print "\n"
    return result


def test():
    import sys, time

    for i in range(5):
        sys.stdout.write(str(i) * (5 - i) + '\r')
        sys.stdout.flush()
        time.sleep(1)

if __name__ == '__main__':
    # password = getpass(prompt='\bplease input your username(there should contains no space):')
    # print password
    test()