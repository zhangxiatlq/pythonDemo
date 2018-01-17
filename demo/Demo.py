listA= ['  xiaohong  ','  xiagonming ',' dapeng ',12343]
tinylist = [' daxing ',20.4]

def foo():
    str="function"
    print(str);

def foo1(num):
    print('num' ,num);

def foo2(name ,age):
    print('name' ,name);
    print('age' ,age);

def linkMethod(list1,list2):
    print(list1 + list2);

#截取list对象的numStar至numEnd之间的内容
def subListMethod(listing,numStar,numEnd):
    print(listing[numStar:numEnd]);

def test():
    numbers = [12,4,5,6,7,8,9,25]
    env = []
    odd = []
    while len(numbers)>0 :
        number = numbers.pop()
        if(number%2==0):
            env.append(number)
        else:
            odd.append(number)
    print(env);

#九九乘法表
def mulTable():
    i = 1
    while i:
        j = 1
        while j:
            print (i,"*",j," = ",i*j,'  ', end='')#end后不会换行
            if(j==i):
                break
            j+=1
            if(j>=10):
                break
        i += 1
        print(" ")
        if(i>9):
            break
    print("乘法表输出完毕")

# 冒泡排序# 定义列表 list
def sort():
    arays = [1,8,2,6,3,9,4]
    for i in range(len(arays)):
        for j in range(i+1):
            if arays[i] < arays[j]:
                arays[i],arays[j] = arays[j],arays[i] # 实现连个变量的互换
    print(arays);


#菲波那切数列
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


if __name__=="__main__":
    # print("main")
    # foo2('yuhui' ,30)
    # foo1(6)
    # foo()
    # linkMethod(listA,tinylist)
    # subListMethod(listA,2,4)
    # print("--------------------------")
    # test()
    # print("--------------------------")
    # mulTable()
    # print("--------------------------")
    # sort()
    print("--------------------------")
    fab(100)