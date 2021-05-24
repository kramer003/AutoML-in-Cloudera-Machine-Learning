# AutoML in Cloudera Machine Learning
The following step-by-step instructions will help you get up and running with AuotML in Cloudera Machine Learning (CML). To learn more about CML, view our **[documentation](https://docs.cloudera.com/machine-learning/cloud/index.html)**

### 0. AutoML Overview
In the following example, we show how CML can be used to build an end-to-end Churn prediction project:
https://github.com/cloudera/CML_AMP_Churn_Prediction

The most complicated part of the project is defining our pipeline, which defines the steps necessary to prepare the data and train the model
```
pipe = Pipeline([("ct", ct), ("scaler", StandardScaler()), ("clf", clf)])
```
In this case, we perform One Hot Encoding to convert character variables to their numeric equivalent, standardize the numeric data, and then train a Logistic Regression. This is all for one model. What if we want to train additional models across various parameter configurations to identify the best model? Imagine how complicated this can get!

AutoML libraries, such as **[H2O](https://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html)** and **[auto-sklearn](https://automl.github.io/auto-sklearn/master/)**, allowing you to simply define your target and predictor variables, and takes care of the rest on the back end.

### 1. Install Dependencies
The [`requirements.txt`](https://github.com/kramer003/AutoML-in-Cloudera-Machine-Learning/blob/main/requirements.txt) file installs dependencies to your CML environment when it starts up. CML comes pre-packaged with common packages such as Pandas and Scikit-learn, we will need to add the `h2o` library to this file. To ensure reproducability, be sure to specify the version of the h2o library you with to install. The most recent h2o verison can be found **[here](https://pypi.org/project/h2o/)**:

#### Example:
`h2o==3.32.1.3`

### 2. Model Building
The [`1_model_building.py`](https://github.com/kramer003/AutoML-in-Cloudera-Machine-Learning/blob/main/code/1_model_building.py) file walks you through the steps of using H2O AutoML.

The Python variable `aml` contains the leaderboard of all models built, and their respective results. In this case the best model is a stacked ensemble.

`aml.leaderboard`
![data](images/leaderboard.png)

`
model_id	auc	logloss	aucpr	mean_per_class_error	rmse	mse
StackedEnsemble_AllModels_AutoML_20210524_160108	0.789456	0.549799	0.807	0.319887	0.431825	0.186473
StackedEnsemble_BestOfFamily_AutoML_20210524_160108	0.788442	0.550816	0.805909	0.326525	0.432312	0.186894
GBM_5_AutoML_20210524_160108	0.78219	0.558353	0.801738	0.319658	0.435512	0.18967
GBM_2_AutoML_20210524_160108	0.777673	0.562514	0.796364	0.334056	0.437583	0.191479
GBM_1_AutoML_20210524_160108	0.777294	0.562744	0.799184	0.356261	0.437727	
`

