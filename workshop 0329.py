import os
#???
os.system("pasue")

#name error
# print (a)
#NameError: name 'a' is not defined on line 1


print ("1"+"1")
# 11

#try:
    
    #嘗試執行的程式碼
#except:
    
    #遇到特定的例外發生時要執行的程式碼
#else:
    
    #若try執行後沒有問題要執行的程式碼
#finally:
    #...?


#當一直在ctrl c+v 就考慮一下是不是要用loop ()

TB = ["John", "Paul", "Ringo", "George"]

print (TB)
for i in range (0, 3, 1):
    print(TB[i])
    
TB = ["John", "Paul", "Ringo", "George"]
print (TB)
for i in range(len(TB)):
    print(TB[0:3:2])  #會重複第0項-第3項兩個一跳重複
    
    
#len (TB) 的原因是因為我們要是不知道TB的長度有些回傳會被miss掉,
#len(var) 是為了讓data保持彈性
print(TB[0:])
print(range(len(TB)))
# len =  length (word count), the result will be a number
a = "abcde"
print(len(a))
    

for i in range(5):
    for j in range(3):
        print(j)
        
#range後面接一個有限範圍

for i in ['a', 'b', 'c']:
    for j in range(3):
        print(j)  


# while + expression 只要.......

i = 0
while i > 5: #true/ false
    print(i)
    i += 2
    
for h in range(10):
    print(h)
    
for i in range(13):
    if i % 3 == 0:
       print("{}!".format(i))
    else:
        print(i)
        
#break - 跳出迴圈

for i in range(13):
    if i % 3 == 0:
       print("{}!".format(i))
       break
    else:
        print(i)
        
for i in range(0, 100):
    if "3" in str(i):
        print("{} there is 3".format(i))
    elif "2" in str(i):
            print("{} there is 2".format(i))        
    else:
        print(i)
        continue  #直接開始下一個loop
    print ('ok')

# pass - 甚麼都不做 直接跳過

#計算機
#1 可以持續使用/ 按Q退出
#2 數字之外
#3 分母為0