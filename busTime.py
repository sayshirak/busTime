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
from matplotlib.pyplot import MultipleLocator
_rebuild()

def statistics():
    busTimeDat = np.loadtxt('busTime.csv',delimiter=',')
    xAxis = busTimeDat[0:, 0]
    yAxis = busTimeDat[0:, 1]
    width = 2

    #计算X轴最大值，方法是Y轴最后一个不为0的值对应的X轴的值再乘以1.01
    xMax = 0;
    for i in range(len(yAxis)):
        if yAxis[len(yAxis)-i-1] > 0:
            xMax = xAxis[len(yAxis)-i-1]
            break

    plt.axis([np.min(xAxis)*0.95,xMax*1.02,0,np.max(yAxis)+1]) #设置X轴和Y轴的最大最小值

    plt.bar(xAxis, yAxis, width, color =  'rgb')
    plt.title('空港13下班高峰期时刻统计')
    plt.ylabel('次数')
    plt.xlabel('时刻')

    x_major_locator = MultipleLocator(50)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    for i in range(busTimeDat.shape[0]):
        if yAxis[i] >0 :
            textStr = "%d,%d"%(xAxis[i], yAxis[i])
            plt.text(xAxis[i], yAxis[i]+0.5, textStr, ha='left', va= 'baseline', fontsize=8, rotation = 45)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.show()

if __name__ == '__main__':
    statistics()