#python3 内置函数demo

#sorted() 函数对所有可迭代的对象进行排序操作。
#sort 与 sorted 区别：
#sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

def sortedDemo(listA):
    listB = sorted(listA)
    return listB

if __name__ == "__main__":
    a = [5,4,9,2,1,6,7]
    print(sortedDemo(a))
