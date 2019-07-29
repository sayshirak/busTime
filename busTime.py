#-*- coding: UTF-8 -*-
'''
空港13下班高峰期时刻统计
matplotlib教程
https://www.runoob.com/numpy/numpy-matplotlib.html
https://www.matplotlib.org.cn
注释详解
https://blog.csdn.net/qq_30638831/article/details/79938967
鼠标悬停注释：
https://codeday.me/bug/20190304/739549.html
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import _rebuild
_rebuild()

def statistics():
    busTimeDat = np.loadtxt('busTime.csv',delimiter=',')
    xAxis = busTimeDat[0,0:]
    yAxis = busTimeDat[1,0:]
    width = 1
    plt.axis([np.min(xAxis)*0.95,np.max(xAxis)*1.05,0,np.max(yAxis)+1]) #设置X轴和Y轴的最大最小值
    plt.bar(xAxis, yAxis, width, color =  'b')
    plt.title('空港13下班高峰期时刻统计')
    plt.ylabel('次数')
    plt.xlabel('时刻')
    for i in range(busTimeDat.shape[1]):
        textStr = "%d,%d"%(xAxis[i],yAxis[i])
        plt.text(xAxis[i],yAxis[i]+0.3,textStr,ha='left', va= 'top',fontsize=8, style='italic', rotation=45)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.show()

if __name__ == '__main__':
    statistics()