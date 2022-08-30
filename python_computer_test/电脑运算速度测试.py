# -*- coding = utf-8 -*-
# @Time : 2022/8/10 10:17
# @Author : 张
# @File : 电脑运算速度测试.py
# @Software : PyCharm
import time

x=0
for i in range(20):
    start_time = time.time()
    while True:
        x = x + 1
        final_time = time.time()
        use_time = final_time - start_time
        if use_time >= 1:
            break
    if i==0:
        a=x
    elif i==1:
        b=x
    elif i==2:
        c=x
    elif i==3:
        d=x
    elif i==4:
        e=x
x=a+b+c+d+e
x=x/5
print('用时{}'.format(use_time),'x={}'.format(x))