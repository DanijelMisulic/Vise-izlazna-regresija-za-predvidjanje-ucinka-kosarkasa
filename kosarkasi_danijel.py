# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from matplotlib import pyplot
import matplotlib.pylab as plt
from sklearn import linear_model
dateparse = lambda dates: pd.datetime.strptime(dates, '%d.%m.%Y %H:%M')
from statsmodels.tsa.arima_model import ARIMA
import warnings
warnings.filterwarnings("ignore")

#%%
data_all = pd.read_csv('C:/Users/Danijel/Desktop/STATISTIKA.csv', delimiter=',', index_col=None, 
                       parse_dates=['datum'], date_parser=dateparse)
data_all = data_all[['datum','tim','igrač','koševi']]

test_data_count = 10

#%%
for team in data_all['tim'].unique():
	data_team = data_all[data_all['tim']==team]
	data = data_team.pivot(index=['datum'],columns='igrač',values='koševi')
	top_5_players = data.count().sort_values(ascending=False)[:5].index
	data = data.loc[:,top_5_players]
	data = data.dropna()
	predicted_data = pd.DataFrame(columns=data.columns, index=data.index)

	for player in data.columns:
		data_player = data.loc[:,player].dropna()
		player_mean = data_player.mean()
		data_player = (data_player - player_mean)
		model = ARIMA(data_player, order=(5, 1, 1))  
		results_AR = model.fit(disp=-1)  
		predictions = player_mean - results_AR.fittedvalues
		predicted_data[player] = predictions

#%%
	X = predicted_data[1:]
	Y = data[1:]
	train_X,test_X = X[:-test_data_count], X[-test_data_count:]
	train_Y,test_Y = Y[:-test_data_count], Y[-test_data_count:]
	multi_target_predictions = pd.DataFrame(columns=test_Y.columns, index=test_Y.index)
	for player in data.columns:
		model = linear_model.LinearRegression()
		model.fit(train_X, train_Y[player])
		predictions = model.predict(test_X)
		multi_target_predictions[player] = predictions

	mae1 = (test_X-test_Y).abs().mean().mean()
	mae2 = (multi_target_predictions-test_Y).abs().mean().mean()
	print(team,round(mae1,2),round(mae2,2),round(Y.corr().abs().mean().mean(),2))
	
