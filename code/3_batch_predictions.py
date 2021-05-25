#Part 3: Batch Predictions

#Load libraries
import h2o
import pandas as pd
from datetime import datetime

#Initialize h2o
h2o.init()

#Load model
auto_model = h2o.load_model('models/StackedEnsemble_AllModels_AutoML_20210525_100709')

#Load Data to Score
df = h2o.import_file("data/WA_Fn-UseC_-Telco-Customer-Churn-.csv")
df.head()

#Generate Predictions
preds = auto_model.predict(df)
preds.head()

#Generate unique time stamp
path = 'data/predictions_' + str(datetime.now().strftime("%Y-%m-%d_%H_%M")) + '.csv'

#Save Predictions with unique time stamp
h2o.export_file(preds, path)