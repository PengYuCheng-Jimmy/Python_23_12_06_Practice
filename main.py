##Q1.輸入一數字判斷是否整數，其為偶數或奇數。
#import sys
#
#number = input("請輸入需要判定的整數：")
#if float(number)%1 != 0:
#    sys.exit("您輸入的數字不是整數")
#if int(number)%2 == 0:
#    print("您輸入的數字為偶數")
#else:
#    print("您輸入的數字為奇數")


#Q2.輸入一個年份，判斷該年是否為閏年。
#第一個規則:年份是4的倍數。
#第二個規則:公元年份為100的倍數為平年。
#第三個規則:公元年份為400的倍數，（1600年及2000年）為閏年。

year = int(input("請輸入一個您想判斷是平年或閏年的西元年："))
if year % 400 == 0:
    print("您輸入的年份為閏年")
    import sys
    sys.exit()
    #sys.exit("您輸入的年份為閏年")
if year % 100 == 0:
    print("您輸入的年份為平年")
    quit()
if year % 4 == 0:
    print("您輸入的年份為潤年")
    exit()
else:
    print("您輸入的年份為平年")

#year = int(input("請輸入一個您想判斷是平年或閏年的西元年："))
#nameOfYear = "平年"
#if year % 4 == 0:
#    nameOfYear = "閏年"
#if year % 100 == 0:
#    nameOfYear = "平年"
#if year % 400 == 0:
#    nameOfYear = "閏年"
#print("西元"+str(year)+"年是"+nameOfYear)