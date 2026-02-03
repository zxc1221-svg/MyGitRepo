'''var1=15
if var1 >= 10:
    print("condition is true")
    print("條件為真")
print("結束條件判斷")

'''
'''
var1=9

if var1 >= 10:
    print("condition is true")
    print("條件為真")
else:
    print("condition is false")
print("結束條件判斷")
'''



'''
var1=9

if var1 >= 20:
    print("this condition is true")
elif var1 >= 10:
    print("this condition is true")
else:
    print("conditions are false")
print("結束條件判斷")   


'''




'''
for i in range(11):
    print("i = " + str(i))
'''

'''
i=1
while i <= 10:
    print("i = " + str(i))
    i = i+1
'''




'''
if i > 5:
    break


if i % 2 == 0:
    continue
'''








'''
def BMI(para1, para2)->float:
    height=para1/100
    weight=para2
    bmi=weight/(height*height)
    return bmi
 
height=float(input("請輸入身高(公分):"))
weight=float(input("請輸入體重(公斤):"))
bmi=BMI(height,weight)
print("BMI=" + str(bmi))

    
if bmi<18.5:
    print("體重過輕")
elif bmi>=18.5 and bmi<24:
    print("體重正常")
elif bmi>=24 and bmi<27:
    print("體重過重")
else:
    print("體重肥胖")

#使用函式製作BMI計算器
'''


 
