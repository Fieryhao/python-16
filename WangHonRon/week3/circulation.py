# author: bruwon
# date:2018-10-12
# for 
#��ϰһ����ӡ����2018-10-12
print(">>>��������������������1��������û���������ص���������")

for i in range(1,100):
    if i<4: 
        print(i)
    if (not i%2==0) and (not i%3==0) and i!=1: 
        print(i)  
#��ϰ������ӡ20��쳲���������2018-10-13
print(">>>쳲��������У�ǰ������Ϊ1���ӵ����ʼ��ÿ��������ǰ������ӡ�")
a=1
b=1
c=0
print(a)
print(b)
for i in range(1,20):
    c=a+b
    a=b
    b=c
    print(c)