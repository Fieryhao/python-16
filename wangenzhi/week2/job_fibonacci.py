# 打印100以内斐波那契数列方法1
a = 0
b = 1

while b < 100:
    print(b)
    c = a + b
    a = b
    b = c
    
