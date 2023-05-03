import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

cd_data = pd.read_csv('creditcard.csv')

# types of data and general info
# cd_data.info()

# number of missing values in each column
cd_data.isnull().sum()

# distribution
cd_data['Class'].value_counts()

# separating the data for analysis

legit = cd_data[cd_data.Class == 0]
fraud = cd_data[cd_data.Class == 1]

legit.shape
fraud.shape

# statical measures of the data
legit.Amount.describe()
fraud.Amount.describe()

# compare the values
cd_data.groupby('Class').mean()

# Under-Sampling
# Creating sample dataset
legit_sample = legit.sample(n=492)

# Concatenating two dataframes
new_data = pd.concat([legit_sample, fraud], axis=0)
# Split data into features and targets
X = new_data.drop(columns='Class', axis=1)
Y = new_data['Class']
jmnwa6
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)

# Model training
# Logistic regression model
model = LogisticRegression()
# Train the LogisticRegression Model with training data
model.fit(X_train, Y_train)

# Model Evaluation
#Accuracy score
#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print(training_data_accuracy)

# Accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print(test_data_accuracy)