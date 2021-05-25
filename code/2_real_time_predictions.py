#Part 2: Real Time Predictions

#Install dependencies
!pip3 install -r requirements.txt

#Load libraries
import h2o
import pandas as pd

#Initialize h2o
h2o.init()

#Load model
auto_model = h2o.load_model('models/StackedEnsemble_AllModels_AutoML_20210525_100709')

def predict(data):

	#Convert JSON data to h2o frame
	df = pd.DataFrame([data])
	df_h2o = h2o.H2OFrame(df)

	#Predictions
	pred = auto_model.predict(df_h2o)
	pred_dict = pred.as_data_frame().to_dict()
	pred_churn = round(pred_dict['Yes'][0],4)

	return {"Probability of Churn": pred_churn}
