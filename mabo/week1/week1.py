#! /usr/bin/python
#  _#_ coding:utf-8 _#_
#  __author__ = "Fieryhao"
#  Date: 2018-12-26 9:08

#  作业1
'''
第一种
'''
a = input('第一个数：')
b = input('第二个数：')
if a>b:
    print(a)
elif b>a:
    print(b)
else:
    print(a)
    print('两者相同')

'''
第二种
当a为0是有bug
'''
i = int(input('第一个数：')) // int(input('第二个数：'))

if i>0:
    print(a)
elif i<0:
    print(b)
else:
    print(a)

# '''
# 第三种
# '''
i = max(int(input('第一个数：')), int(input('第二个数：')))
print(i)



'''
第四种
'''
a = input('第一个数：')
b = input('第二个数：')
if a>=b:  # else可以整合到 >中
    print(a)
elif b>a:
    print(b)
    
    
    
    
 #  作业2
 #! /usr/bin/python
#  _#_ coding:utf-8 _#_
#  __author__ = "Fieryhao"
#  Date: 2018-12-26 10:56

'''
判断输入的5为以内的整数，判断几位。
'''


'''第一种'''
I = input("请输入整数:")
print(len(I))

'''第二种'''
I = int(input("请输入整数:"))
if I<10:
    print(1)
elif I <100:
    print(2)
elif I <1000:
    print(3)
elif I <10000:
    print(4)
else:
    print(5)

'''第三种'''
I = int(input("请输入整数:"))
a = 0
while I >=1:
    I = I // 10
    a += 1
print(a)
    
   
