# AutoML in Cloudera Machine Learning
The following step-by-step instructions will help you get up and running with AuotML in Cloudera Machine Learning (CML). To learn more about CML, view our **[documentation][https://docs.cloudera.com/machine-learning/cloud/index.html]**

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
The `requirements.txt` file allows you to install dependencies when CML starts up. CML comes pre-packaged with common packages such as Pandas and Scikit-learn, we will need to add the `h2o` library to this file. To ensure reproducability, be sure to specify the version of the h2o library you with to install. The most recent verison can be found **[Here](https://pypi.org/project/h2o/)**:
![data](images/requirements.png)