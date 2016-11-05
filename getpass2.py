# coding:utf-8
import sys, os
from time import *

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/10/15'
#    __Desc__ =   just like getpass lib, this is also simple and easy to use. While the drawback is it's not so much pythonic in the implement of the function 'replace'.
#                  I am happy to hear you can join me to slove it. :)
#                 改进版的getpass，更易用，更好用！ 唯一的缺点就是replace函数中的实现略显粗糙，欢迎前来完善。

# show the numbers we have typed
def showByNumbers(prompt='', tip = 'You have typed %d characters!'):
    # print the prompt to prompt user what to do
    print prompt
    import msvcrt
    # get one charecter from terminal
    cur_character = msvcrt.getch()
    # the result will be out final answer!
    result =''+cur_character
    count = 1
    # 循环的读取从控制台输入的字符数据 get character once a time from terminal
    while cur_character!= '\r':
        # show message at the old line with the help of  the function named sys.stdout.write and sys.stdout.flush
        sys.stdout.write(tip%(count)+"\r")
        sys.stdout.flush()
        # update the needed item
        cur_character = msvcrt.getch()
        if cur_character =="\b":
            result = result[0:-1]
            count -=1
        else:
            result += cur_character
            count += 1
    # to avoid overlap the message, we'd better go to next new line.
    print "\n"
    # return what we really need
    return result

# use the constom char to replace what we typed
def replaceWithDelimiter(prompt='', delimiter = '*'):
    print prompt
    import msvcrt

    current_character = msvcrt.getch()
    count = 1
    result = ''
    result += current_character

    # if we typed backspace key, we should update the interface right now!
    delta = 0

    # get a character once a time and do something if meet the backspace
    while current_character!='\r':
        # build the stars to show
        stars = ''
        for index in range(count):
            stars += delimiter
            for i in range(delta):
                stars += ' '
        sys.stdout.write(prompt + stars + "\r")
        sys.stdout.flush()

        # update for next loop
        current_character = msvcrt.getch()
        # consider the backspace key
        if current_character == '\b':
            count -=1
            result = result[0:-1]
            # for erase the extra delimiters
            delta +=1
        else:
            result += current_character
            count +=1

    # it's necessary to print in a new line for avoiding overlapping
    print "\n"
    # return what we really need
    return result


def getpass(prompt='', mode='n', tip='You have typed %d characters!', delimiter='*'):

    if mode =='n':
        return showByNumbers(prompt=prompt, tip=tip)
    elif mode == 'r':
        return replaceWithDelimiter(prompt=prompt, delimiter=delimiter)
    else:
        raise NameError('There are only two choice, so check your input!')

if __name__ == '__main__':
    """
    Here are some useful test. And you can also do it just like this!
    :)
    """
    # password = getpass(prompt='\bplease input your username(there should contains no space):')
    # print password
    # password = replaceWithDelimiter(prompt='\bplease input your username(there should contains no space):', delimiter='')
    # print password
    password = getpass(prompt='\bplease input your username(there should contains no space):', mode='n')
    print password

    pwd = getpass(prompt='\bplease input your username(there should contains no space):', mode='r', delimiter='#')
    print pwd
