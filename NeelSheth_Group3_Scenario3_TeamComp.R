library(tidyverse)
library(quantmod)
library(rvest)
library(lubridate)
library(forecast)

# Get data and transform into quarterly time series
getSymbols("HOUSTNSA",src="FRED")
HOUSTNSA.df = data.frame(Date = index(HOUSTNSA), HOUSTNSA = as.numeric(HOUSTNSA))
y = ts(HOUSTNSA,start=c(1959,1),frequency=12)
quarterly = aggregate(y, nfrequency = 4)
dfquarterly = data.frame(quarterly)

train = window(quarterly, end = c(2006, 4))
N = length(quarterly) - length(train)
Ntrain = length(train)
train = window(quarterly,start=c(1959,1),end=c(1959,Ntrain)) 
test = window(quarterly,start=c(1959,Ntrain+1),end=c(1959,Ntrain+1))

# M1 - ETS
model_accuracy_ets = NULL 
M1means = NULL
for(i in 1:N){
  train = window(quarterly,end=c(1959,Ntrain+i-1))
  test = window(quarterly,start=c(1959,Ntrain+i),end=c(1959,Ntrain+i))
  M1 = ets(train, lambda = "auto")
  M1F = forecast(M1, h = length(test), level = 95)
  model_accuracy_ets = rbind(model_accuracy_ets,accuracy(M1F,test)[,c("RMSE","MAPE")])
  M1means = as.data.frame(rbind(M1means, M1F$mean))
  print(i)
}
M1meanTS = ts(M1means$`sign(xx)`, start = c(2007,1), frequency = 4)

ets_training_rmse = mean(model_accuracy_ets[seq(from = 1, to = nrow(model_accuracy_ets), by = 2), 1])
ets_training_mape = mean(model_accuracy_ets[seq(from = 1, to = nrow(model_accuracy_ets), by = 2), 2])
ets_testing_rmse = mean(model_accuracy_ets[seq(from = 2, to = nrow(model_accuracy_ets), by = 2), 1])
ets_testing_mape = mean(model_accuracy_ets[seq(from = 2, to = nrow(model_accuracy_ets), by = 2), 2])

# M2 - ARIMA
model_accuracy_arima = NULL 
M2means = NULL
for(i in 1:N){
  train = window(quarterly,end=c(1959,Ntrain+i-1))
  test = window(quarterly,start=c(1959,Ntrain+i),end=c(1959,Ntrain+i))
  M2 = auto.arima(train, lambda = "auto")
  # M2 = Arima(train, order = c(2, 0, 0), seasonal = c(0, 1, 1), include.drift = TRUE, lambda = "auto")
  M2F = forecast(M2, h = length(test), level = 95)
  model_accuracy_arima = rbind(model_accuracy_arima,accuracy(M2F,test)[,c("RMSE","MAPE")])
  M2means = as.data.frame(rbind(M2means, M2F$mean))
  print(i)
}
M2meanTS = ts(M2means$`sign(xx)`, start = c(2007,1), frequency = 4)

arima_training_rmse = mean(model_accuracy_arima[seq(from = 1, to = nrow(model_accuracy_arima), by = 2), 1])
arima_training_mape = mean(model_accuracy_arima[seq(from = 1, to = nrow(model_accuracy_arima), by = 2), 2])
arima_testing_rmse = mean(model_accuracy_arima[seq(from = 2,  to = nrow(model_accuracy_arima), by = 2), 1])
arima_testing_mape = mean(model_accuracy_arima[seq(from = 2, to = nrow(model_accuracy_arima), by = 2), 2])

# M3 - NN
model_accuracy_nn = NULL 
M3means = NULL
for(i in 1:N){
  train = window(quarterly,end=c(1959,Ntrain+i-1))
  test = window(quarterly,start=c(1959,Ntrain+i),end=c(1959,Ntrain+i))
  M3 = nnetar(train,lambda = "auto")
  M3F = forecast(M3, h = length(test), level = 95)
  model_accuracy_nn = rbind(model_accuracy_nn,accuracy(M3F,test)[,c("RMSE","MAPE")])
  M3means = as.data.frame(rbind(M3means, M3F$mean))
  print(i)
}
M3meanTS = ts(M3means$`sign(xx)`, start = c(2007,1), frequency = 4)

nn_training_rmse = mean(model_accuracy_nn[seq(from = 1, to = nrow(model_accuracy_nn), by = 2), 1])
nn_training_mape = mean(model_accuracy_nn[seq(from = 1, to = nrow(model_accuracy_nn), by = 2), 2])
nn_testing_rmse = mean(model_accuracy_nn[seq(from = 2, to = nrow(model_accuracy_nn), by = 2), 1])
nn_testing_mape = mean(model_accuracy_nn[seq(from = 2, to = nrow(model_accuracy_nn), by = 2), 2])

# M4 - Naive
model_accuracy_naive = NULL 
M4means = NULL
for(i in 1:N){
  train = window(quarterly,end=c(1959,Ntrain+i-1))
  test = window(quarterly,start=c(1959,Ntrain+i),end=c(1959,Ntrain+i))
  M4F = snaive(train,h=length(test))
  model_accuracy_naive = rbind(model_accuracy_naive,accuracy(M4F,test)[,c("RMSE","MAPE")])
  M4means = as.data.frame(rbind(M4means, M4F$mean))
  print(i)
}
M4meanTS = ts(M4means$V1, start = c(2007,1), frequency = 4)

naive_training_rmse = mean(model_accuracy_naive[seq(from = 1, to = nrow(model_accuracy_naive), by = 2), 1])
naive_training_mape = mean(model_accuracy_naive[seq(from = 1, to = nrow(model_accuracy_naive), by = 2), 2])
naive_testing_rmse = mean(model_accuracy_naive[seq(from = 2, to = nrow(model_accuracy_naive), by = 2), 1])
naive_testing_mape = mean(model_accuracy_naive[seq(from = 2, to = nrow(model_accuracy_naive), by = 2), 2])

# M5 - TSLM
model_accuracy_tslm = NULL 
M5means = NULL
for(i in 1:N){
  train = window(quarterly,end=c(1959,Ntrain+i-1))
  test = window(quarterly,start=c(1959,Ntrain+i),end=c(1959,Ntrain+i))
  M5 = tslm(train ~ trend + season, lambda = "auto")
  M5F = forecast(M5, h = length(test), level = FALSE)
  model_accuracy_tslm  = rbind(model_accuracy_tslm ,accuracy(M5F,test)[,c("RMSE","MAPE")])
  M5means = as.data.frame(rbind(M5means, M5F$mean))
  print(i)
}
M5meanTS = ts(M5means$`sign(xx)`, start = c(2007,1), frequency = 4)

tslm_training_rmse = mean(model_accuracy_tslm[seq(from = 1, to = nrow(model_accuracy_tslm), by = 2), 1])
tslm_training_mape = mean(model_accuracy_tslm[seq(from = 1, to = nrow(model_accuracy_tslm), by = 2), 2])
tslm_testing_rmse = mean(model_accuracy_tslm[seq(from = 2, to = nrow(model_accuracy_tslm), by = 2), 1])
tslm_testing_mape = mean(model_accuracy_tslm[seq(from = 2, to = nrow(model_accuracy_tslm), by = 2), 2])

# M6 - Theta
model_accuracy_theta = NULL 
M6means = NULL
for(i in 1:N){
  train = window(quarterly,end=c(1959,Ntrain+i-1))
  test = window(quarterly,start=c(1959,Ntrain+i),end=c(1959,Ntrain+i))
  M6F = thetaf(train, h=length(test))
  model_accuracy_theta = rbind(model_accuracy_theta,accuracy(M6F,test)[,c("RMSE","MAPE")])
  M6means = as.data.frame(rbind(M6means, M6F$mean))
  print(i)
}
M6meanTS = ts(M6means$X, start = c(2007,1), frequency = 4)

theta_training_rmse = mean(model_accuracy_theta[seq(from = 1, to = nrow(model_accuracy_theta), by = 2), 1])
theta_training_mape = mean(model_accuracy_theta[seq(from = 1, to = nrow(model_accuracy_theta), by = 2), 2])
theta_testing_rmse = mean(model_accuracy_theta[seq(from = 2, to = nrow(model_accuracy_theta), by = 2), 1])
theta_testing_mape = mean(model_accuracy_theta[seq(from = 2, to = nrow(model_accuracy_theta), by = 2), 2])

# M7 - CTSD
model_accuracy_ctsd = NULL 
M7means = NULL
for(i in 1:N){
  train = window(quarterly,end=c(1959,Ntrain+i-1))
  test = window(quarterly,start=c(1959,Ntrain+i),end=c(1959,Ntrain+i))
  M7F = stlf(train, h = length(test), lambda = "auto")
  model_accuracy_ctsd = rbind(model_accuracy_ctsd,accuracy(M7F,test)[,c("RMSE","MAPE")])
  M7means = as.data.frame(rbind(M7means, M7F$mean))
  print(i)
}
M7meanTS = ts(M7means$`sign(xx)`, start = c(2007,1), frequency = 4)

ctsd_training_rmse = mean(model_accuracy_ctsd[seq(from = 1, to = nrow(model_accuracy_ctsd), by = 2), 1])
ctsd_training_mape = mean(model_accuracy_ctsd[seq(from = 1, to = nrow(model_accuracy_ctsd), by = 2), 2])
ctsd_testing_rmse = mean(model_accuracy_ctsd[seq(from = 2, to = nrow(model_accuracy_ctsd), by = 2), 1])
ctsd_testing_mape = mean(model_accuracy_ctsd[seq(from = 2, to = nrow(model_accuracy_ctsd), by = 2), 2])

# Put all scores in one table
cbind_ets = cbind(
  round(ets_training_rmse,2),
  round(ets_training_mape,2),
  round(ets_testing_rmse,2),
  round(ets_testing_mape,2)
)

cbind_arima = cbind(
  round(arima_training_rmse,2),
  round(arima_training_mape,2),
  round(arima_testing_rmse,2),
  round(arima_testing_mape,2)
)

cbind_nn = cbind(
  round(nn_training_rmse,2),
  round(nn_training_mape,2),
  round(nn_testing_rmse,2),
  round(nn_testing_mape,2)
)

cbind_naive = cbind(
  round(naive_training_rmse,2),
  round(naive_training_mape,2),
  round(naive_testing_rmse,2),
  round(naive_testing_mape,2)
)

cbind_tslm = cbind(
  round(tslm_training_rmse,2),
  round(tslm_training_mape,2),
  round(tslm_testing_rmse,2),
  round(tslm_testing_mape,2)
)


cbind_theta = cbind(
  round(theta_training_rmse,2),
  round(theta_training_mape,2),
  round(theta_testing_rmse,2),
  round(theta_testing_mape,2)
)

cbind_ctsd = cbind(
  round(ctsd_training_rmse,2),
  round(ctsd_training_mape,2),
  round(ctsd_testing_rmse,2),
  round(ctsd_testing_mape,2)
)

accuracy_model = rbind(
  cbind_ets,
  cbind_arima,
  cbind_nn,
  cbind_naive,
  cbind_tslm,
  cbind_theta,
  cbind_ctsd
)

models = paste0("", c("Smoothing", "ARIMA", "Neural Networks", "Naive",
                      "Regression for Time Series", "Theta",
                      "Classical Time Series Decomposition"))

final_model = data.frame(M = models, accuracy_model)

colnames(final_model)
colnames(final_model)[2:5] = c("Training RMSE", "Training MAPE", "Testing RMSE","Testing MAPE")
final_model

# Visualizations
test = window(quarterly,start=c(2007,1))
autoplot(train, size = 1.5) + autolayer(test, size = 1.5) + 
  autolayer(M1F$fitted, size = 1.5) + autolayer(M1meanTS, size = 1.5) + 
  theme_bw() + ggtitle("ETS") + ylab("Thousands of Units")

autoplot(train, size = 1.5) + autolayer(test, size = 1.5) + 
  autolayer(M2F$fitted, size = 1.5) + autolayer(M2meanTS, size = 1.5) + 
  theme_bw() + ggtitle("ARIMA") + ylab("Thousands of Units")

autoplot(train, size = 1.5) + autolayer(test, size = 1.5) + 
  autolayer(M3F$fitted, size = 1.5) + autolayer(M3meanTS, size = 1.5) + 
  theme_bw() + ggtitle("Neural Network") + ylab("Thousands of Units")

autoplot(train, size = 1.5) + autolayer(test, size = 1.5) + 
  autolayer(M4F$fitted, size = 1.5) + autolayer(M4meanTS, size = 1.5) + 
  theme_bw() + ggtitle("Naive") + ylab("Thousands of Units")

autoplot(train, size = 1.5) + autolayer(test, size = 1.5) + 
  autolayer(M5F$fitted, size = 1.5) + autolayer(M5meanTS, size = 1.5) + 
  theme_bw() + ggtitle("Regression for Time Series") + ylab("Thousands of Units")

autoplot(train, size = 1.5) + autolayer(test, size = 1.5) + 
  autolayer(M6F$fitted, size = 1.5) + autolayer(M6meanTS, size = 1.5) + 
  theme_bw() + ggtitle("Theta") + ylab("Thousands of Units")

autoplot(train, size = 1.5) + autolayer(test, size = 1.5) + 
  autolayer(M7F$fitted, size = 1.5) + autolayer(M7meanTS, size = 1.5) + 
  theme_bw() + ggtitle("Classical Time Series Decomposition") + ylab("Thousands of Units")


# What model would you recommend an economic consulting start up to use for forecasting private housing starts?

# We would recommend using classical time series decomposition. The average RMSE and MAPE was
# pretty low for all four of the scenarios, and it is a simple model that is fairly easy to 
# understand. So, the model is simple, easy to understand, and as accurate if not more accurate
# than some of the other more complex models, so classical time series decomposition is our 
# recommendation. 

