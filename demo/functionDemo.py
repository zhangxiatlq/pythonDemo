#列表翻转函数一
def reverse(li):
    for i in range(0, len(li)//2):
        temp = li[i]
        li[i] = li[-i-1]
        li[-i-1] = temp

#列表翻转函数二
def reverse1(ListInput):
    RevList=[]
    for i in range (len(ListInput)):
        RevList.append(ListInput.pop())#通过默认移除最后一个值，并且返回这个移除值进行填充
    return RevList

#列表翻转简单化
def reverse2(li):
    for i in range(0, len(li)//2):
        li[i], li[-i - 1] = li[-i - 1], li[i]
    return li

#关于 return fun 和 return fun() 的区别
def funx(x):
    def funy(y):
        return x*y;
    return funy #return funy返回的是一个对象，可理解为funx是funy的一个对象
    # return funy()    #return funy()返回的是funy的函数返回值，所以此处报错

def funA(a):
    def funB(b):
        return a*b;
    return funB(10)

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    reverse(l)
    print(l)
    print("------翻转2-------")
    print(reverse1(l))
    ll = [1, 2, 3, 4, 5,6]
    print("------翻转3-------")
    print(reverse2(ll))
    print(funx(5)(10))
    print(funA(10))
