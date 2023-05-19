# Model Card

For additional information see the github: https://github.com/weixinyu/nd0821-c3-starter-code/

## Model Details
Wei Xinyu created the model. It is random forest classication using the default pareameters in 0.24.1

## Intended Use
This model should be used to predict whether the income exceeds $50K/yr based on the publicly available Census Bureau data

## Training Data and Testing Data
The data was obtained from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/census+income). The target class was  from two categories: "<=50K", and ">50K" 
The original data set has 32561 rows, and a 80-20 split was used to break this into a train and test set.  To use the data for training a One Hot Encoder was used on the features and a label binarizer was used on the labels.

## Metrics
The model was evaluated using precision, recall and F1 score. 
Precision: 0.7111111111111111 Recall: 0.6166112956810631 FBeta: 0.6604982206405694

## Ethical Considerations
We treat the attributes in the dataset as the only factors affecting the income, and it is not true in the real case.

## Caveats and Recommendations
This project is to get familiar with the CI/CD process of machine learning, so the performance of the model is not the target of it. You can do model selection and hyperparameter tuning to enhance the performance.
This is a project of Udacity Program and cannot be used for commercial purpose.
