# Answers - Data Challenge
___
### Question 1 (10 Points)
#### List as many use cases for the dataset as possible.


This dataset can be used in a variety of analysis, such as:
1) Churn prediction: predict which customers are likely to leave a service. Acquiring new customers often costs 5 times more than retaining existing ones;
2) Uplift modeling: predict the response of customers to specific treatments, such as marketing campaigns;
3) RFM (Recency, Frequency, Monetary value) analysis: quantitatively ranks and groups customers based on their purchases in a given time period, so that targeted marketing campaigns can be performed;
4) Customer Segmentation: divides a company's customers into groups that reflect similarity among such customers in each group, which helps maximize the value of each customer to the business;
5) CLV (Customer Lifetime Value) Prediction: predicts the monetary value of a customer with your business over their entire lifetime, i.e., until they churn;
6) Predict Next Purchase Day: predicts the day of the next purchase of a customer by analyzing their purchasing patterns, so that engagement messages can be sent to meet their needs.
___
### Question 2 (10 Points)
#### Pick one of the use cases you listed in question 1 and describe how building a statistical model based on the dataset could best be used to improve the business this data comes from.


Selected case: churn prediction.
Take action towards retaining a customer is often more cheap than acquiring a new one. Thus, it is critical to predict as soon as possible whether a customer will churn or not. If so, targeted action can be taken to avoid churning.

Therefore, it is extremely important to understand what keeps customers engaged with the company.
___
### Question 3 (20 Points)
#### Implement the model you described in question 2, preferably in Python. The code has to retrieve the data, train and test a statistical model, and report relevant performance criteria. Ideally, we should be able to replicate your analysis from your submitted source-code, so please explicit the versions of the tools and packages you are using.


All these steps can be found on notebooks `01_data_analysis` and `02_model_training`, respectively, located in the `src` folder. Both notebooks have all the rationale behind them thoroughly explained, as well as a step-by-step analysis of each cell.
___
### Question 4 (60 Points)
#### 1. Explain each and every of your design choices, you can use jupyter notebooks. (e.g., preprocessing, model selection, hyper parameters, evaluation criteria). Compare and contrast your choices with alternative methodologies.


Design choices and alternative methodologies were all thoroughly explained throughout both notebooks. Please, read them carefully.

#### 2. Describe how you would improve the model in Question 3 if you had more time.
- Better data understanding, by getting in touch with the data engineer or someone from the business. Some columns are not properly described, and they can heavily interfere (positively or negatively) in the model. Also, it is not clear if this is a contractual (has "churn events") or non-contractual churn (analyzes timespans);
- Gather more data. Churn prediction is a very difficult task, and there is no consensus in the literature about the core features that should be taken into account when modeling it. However, the given data is too simple, which affects model predictions (the generated features are not good at predicting the labels);
- Improve data analysis. Good data is more important than cutting-edge models. Checking if no values are wrongly placed or out of bonds, such as negative values for positive-only features or wrong dates, etc. is mandatory;
- Better research on the topic. Churn prediction has a lot of small details and specificities that makes it hard to model;
- Improve feature engineering and feature selection. Selecting relevant features is imperative for a good machine learning model. Efficient feature engineering leads to reduced computational efforts, better model performance, better quality of the output obtained from the models, etc.;
- Analyze more classification models and train them using not just their default hyperparameters. The models trained in this case were instantiated using their default hyperparameters, which is a decent approach for initial analysis, but not deep enough to fully reject the unfeasibility of a given model;
- Perform a grid search or random search. These are powerful tools that exhaustively search for the best hyperparameters, but with high computational costs. Performing them on a few selected models would boost their metrics.