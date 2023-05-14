# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


legends = ['时空交互图模型', 'ORCA模型', '社会力模型', '', '']

# add any folder directories here!
# log_list = [
# pd.read_csv("trained_models/GST_predictor_non_rand/progress.csv"),
# pd.read_csv("trained_models/GST_predictor_rand/progress.csv"),
# pd.read_csv("trained_models/my_modeldemo1/progress.csv"),
# 	]
log_list = [
pd.read_csv("trained_models/GST_predictor_non_rand/progress.csv"),
pd.read_csv("trained_models/hengsu/progress.csv"),
pd.read_csv("trained_models/nonpredictor/progress.csv"),
	]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'AR PL UKai CN'
plt.rcParams['axes.unicode_minus']=False 

logDicts = {}
for i in range(len(log_list)):
	logDicts[i] = log_list[i]

graphDicts={0:'eprewmean', 1:'loss/value_loss'}
graphDicts1={0:'平均奖励函数曲线', 1:'损失函数曲线'}
legendList=[]
# summarize history for accuracy

# for each metric
for i in range(len(graphDicts)):
	plt.figure(i)
	plt.title(graphDicts1[i])
	j = 0
	for key in logDicts:
		if graphDicts[i] not in logDicts[key]:
			continue
		else:
			plt.plot(logDicts[key]['misc/total_timesteps'],logDicts[key][graphDicts[i]])

			legendList.append(legends[j])
			print('avg', str(key), graphDicts[i], np.average(logDicts[key][graphDicts[i]]))
		j = j + 1
	print('------------------------')
    
	plt.xlabel('总时间步长')
	plt.legend(legendList, loc='lower right')
	legendList=[]

plt.show()
