

total = 0; # 这是一个全局变量

sum = lambda var1,var2:var1+var2;

def sum1(var1,var2):
    global total # 使用 global 声明全局变量,定义了全局变量就会改变全局变量值，在函数外面的值也就被修改为函数内部的值
    total = var1+var2;
    print("函数内局部变量total=",total)
    return total;

if __name__ == "__main__":
    print(sum(10,20))
    print(sum1(20,30))
    print("函数外全局变量total=",total)
