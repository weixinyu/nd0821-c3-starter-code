Documentation
-------------
## Motivation for the project
This project is to develop a classification model on publicly available Census Bureau data. There are unit tests to monitor the model performance on various data slices. It also deploys your model using the FastAPI package and create API tests. The slice validation and the API tests will be incorporated into a CI/CD framework using GitHub Actions.

##  Libraries:
numpy - The fundamental package for scientific computing with Python
pandas - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, and most of the data analysis in this project is based on the dataframe in Pandas.
sklearn - This is a simple and efficient tools for predictive data analysis, and the linear regression model in this package is used in this project
pytest - This is a powerful auto test tools for unit tests
requests - This package is to send GET, POST requests
fastapi - This is a very efficient app creation framework
uvicorn - This is a package for deployint the app

## Metrics
The model was evaluated using precision, recall and F1 score. 
Precision: 0.7111111111111111 Recall: 0.6166112956810631 FBeta: 0.6604982206405694

## Acknowledgements
In this project, I have benifited the knowledge from Udacity program MLOPS and worked based on some demo codes in this project.

