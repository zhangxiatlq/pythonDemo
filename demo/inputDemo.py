#文件i/o实例
import os
# -*- coding: UTF-8 -*-
#读取键盘输入值，并打印出来
def inputContent():
    str = input("请输入：");
    print("输入的内容：",str) #默认按enter键结束输入

#获取当前目录信息
def getDir():
    print(os.getcwd()) #显示当前的工作目录



if __name__ == "__main__":
    getDir()
    # 打开一个文件
    fo = open("G://foo.txt", "w+")
    str = fo.read(10);
    print("读取的字符串是 : ", str)

    # 查找当前位置
    position = fo.tell();
    print("当前文件位置 : ", position)

    fo.write("这是我创建的第一个测试文件！\nwelcome!");#先清除文件中所有内容。然后再写入现在的内容

    # 把指针再次重新定位到文件开头
    position = fo.seek(0, 0);
    str = fo.read(10);
    print("重新读取字符串 : ", str)
    # 关闭打开的文件
    fo.close()
