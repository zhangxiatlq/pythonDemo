import time
import calendar
import datetime


# 格式化成2016-03-20 11:45:39形式
dateFormat1 = "%Y-%m-%d %H:%M:%S"
#格式化成Sat Mar 28 22:24:24 2016形式
dateFormat2 = "%a %b %d %H:%M:%S %Y"

def formatToDate(dateFormat):
    print("格式化形式",dateFormat)
    retunContent = time.strftime(dateFormat, time.localtime())
    return retunContent



#将格式字符串转换为时间戳
def formatToNum():
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

#打印某月的月历
def printmonth(year,month):
    print("以下输出",year,"年",month,"月份的日历:")
    cal = calendar.month(year,month)
    print(cal)
    if(calendar.isleap(year)):
        print(year,"年是瑞年")
    else:
        print(year,"年是平年")

#获取date相关内容
def getDate():
    date = datetime.datetime.now()
    print("当前的日期和时间是 %s" %date)
    print("ISO格式的日期和时间是 %s" %date.isoformat() )
    print("当前的年份是 %s" %date.year)
    print("当前的月份是 %s" %date.month)
    print("当前的日期是  %s" %date.day)
    print("dd/mm/yyyy 格式是  %s/%s/%s" % (date.day, date.month, date.year) )
    print("当前小时是 %s" %date.hour)
    print("当前分钟是 %s" %date.minute)
    print("当前秒是  %s" %date.second)

if __name__=="__main__":
    star = time.clock()
    print("当前时间：",time.time())
    localtime = time.localtime(time.time())
    print("当前时间：",localtime)
    localtime = time.asctime(localtime)
    print("当前时间：",localtime)
    formatToNum()
    print("当前时间：",formatToDate(dateFormat1))
    print("当前时间：",formatToDate(dateFormat2))
    printmonth(2018,1)
    getDate()

    end = time.clock()
    print(end-star)

