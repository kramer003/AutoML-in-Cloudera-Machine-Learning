#Part 1: Model Building

#Install dependencies
#You only need to run this once
#Packages available across all future sessions
! pip3 install -r requirements.txt

#Load libraries
import os
import h2o
import pandas as pd
from h2o.automl import H2OAutoML

#Initialize h2o
h2o.init()

#Load Data
df = h2o.import_file("data/WA_Fn-UseC_-Telco-Customer-Churn-.csv")
df.head()

#Create a training and a test dataset
#We will use test data to predict on unseen data
train, test = df.split_frame(ratios=[.7])

#Data Preparation for H2o
#Remove churn from list of predictor variables
#If target is numeric, use .asfactor() to convert to cateogrical
#Our target `churn` is already numeric
x = train.columns
y = "Churn"
x.remove(y)

#Train the Model
auto_ml = H2OAutoML(max_models=10)
auto_ml.train(x=x, y=y, training_frame=train)

#View leaderboard
leaderboard = auto_ml.leaderboard
leaderboard.head(rows=5) 

#Inspect leader model
auto_ml.leader

#Generate predictions on test data using best model
#Can also use auto_ml.leader.predict()
preds = auto_ml.predict(test)
preds.head(5)

#Assess model performance on test data
auto_ml.leader.model_performance(test)

#Save the model state to the file system
#We will use this to generate real-time predictions
h2o.save_model(model=auto_ml.leader, path=os.path.realpath('.') + '/models', force=True)
