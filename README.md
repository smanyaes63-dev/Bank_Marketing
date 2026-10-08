
# Bank Marketing Campaign Response Prediction Using Machine Learning

Project Overview

This project develops a machine learning-based system to predict whether a customer is likely to subscribe to a term deposit as a result of a bank marketing campaign.

The project follows a complete machine learning workflow, including:

- Data understanding
- Exploratory Data Analysis (EDA)
- Data preprocessing
- Feature selection
- Model comparison
- Hyperparameter tuning
- Model evaluation
- Flask-based deployment

A Flask web application was developed to allow users to enter customer and campaign information and receive a subscription prediction along with the predicted probability.

---

Problem Statement

Banks conduct marketing campaigns to promote financial products such as term deposits. Identifying customers who are more likely to subscribe can help banks improve campaign effectiveness and reduce unnecessary marketing efforts.

The objective of this project is to build a classification model that predicts whether a customer will subscribe to a term deposit based on customer and campaign-related information.

---

Dataset

The project uses the Bank Marketing Dataset from the UCI Machine Learning Repository.

- Dataset: Bank Marketing
- Source: UCI Machine Learning Repository
- Instances: 45,211
- Input Features: 16
- Target Variable: "y"
- Problem Type: Binary Classification

Target Variable

Value| Meaning
"no"| Customer did not subscribe
"yes"| Customer subscribed

The dataset is imbalanced, with approximately:

- 88.30% → "no"
- 11.70% → "yes"

---

Features

The dataset contains the following input features:

Numerical Features

- Age
- Account Balance
- Day of Contact
- Call Duration
- Campaign Contacts
- Days Since Previous Contact
- Previous Contacts

Categorical Features

- Job
- Marital Status
- Education
- Credit Default
- Housing Loan
- Personal Loan
- Contact Type
- Month
- Previous Campaign Outcome

---

Exploratory Data Analysis

The following analyses were performed:

- Target variable distribution
- Categorical feature distributions
- Numerical feature distributions
- Histogram analysis
- KDE analysis
- Boxplot analysis
- Numerical features vs target
- Categorical features vs target
- Correlation analysis
- Correlation heatmap
- Outlier investigation

The analysis identified class imbalance, skewed numerical features, meaningful sentinel values such as "pdays = -1", and differences between customers who subscribed and those who did not.

---

Data Preprocessing

Categorical Features

One-Hot Encoding was applied to categorical features using:

- "OneHotEncoder"
- "drop="first""
- "handle_unknown="ignore""

Numerical Features

Numerical features were standardized using:

- "StandardScaler"

The scaler was fitted only on the training data to avoid data leakage.

---

Feature Selection

Two feature selection techniques were explored.

Random Forest Feature Importance

Random Forest feature importance was used to identify features that contributed strongly to prediction.

SelectKBest

"SelectKBest" with the "f_classif" scoring function was used to select the top 10 transformed features.

---

Machine Learning Models

Six classification algorithms were compared:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. K-Nearest Neighbors
5. Support Vector Machine
6. Gradient Boosting

---

Model Comparison

Model| Accuracy| ROC-AUC
Logistic Regression| 90.12%| 89.66%
Decision Tree| 88.52%| 69.75%
Random Forest| 88.95%| 84.98%
KNN| 89.43%| 83.16%
SVM| 90.25%| 81.11%
Gradient Boosting| 90.26%| 90.48%

Gradient Boosting achieved the strongest overall ROC-AUC performance and was selected for further hyperparameter tuning.

---

Hyperparameter Tuning

"GridSearchCV" was used to optimize the Gradient Boosting model.

The selected hyperparameters were:

n_estimators = 150
learning_rate = 0.1
max_depth = 3

These parameters were selected through grid-search-based hyperparameter optimization.

---

Final Model

The final prediction system uses the Gradient Boosting Classifier.

The model predicts whether a customer is likely to subscribe to a term deposit and provides a probability associated with the prediction.

The final workflow is:

Customer Input
      ↓
Data Preprocessing
      ↓
Feature Transformation
      ↓
Feature Selection
      ↓
Gradient Boosting Model
      ↓
Prediction
      ↓
Subscription Probability

---

Evaluation Metrics

The models were evaluated using:

- Accuracy
- ROC-AUC

Accuracy

Accuracy measures the proportion of correctly classified observations out of all observations.

ROC-AUC

ROC-AUC measures the model's ability to distinguish between customers who subscribe and those who do not.

For this project, ROC-AUC was given particular importance because the dataset is imbalanced.

---

Flask Web Application

A Flask-based web application was developed for model deployment.

The application allows users to enter customer and campaign information through a web interface.

The application then:

1. Accepts customer information.
2. Processes the input data.
3. Applies the trained preprocessing pipeline.
4. Passes the transformed data to the trained model.
5. Generates a prediction.
6. Displays the predicted subscription probability.

Application Output

The application provides a prediction indicating whether the customer is likely to subscribe to the term deposit.

---

Project Structure

Bank-Marketing-Campaign-Prediction/
│
├── notebook/
│   └── Bank_Marketing_Project.ipynb
│
├── model/
│   └──bank_marketing_final_pipeline.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── requirements.txt

---

Technologies Used

Programming Language

- Python

Libraries

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- Joblib

Machine Learning

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors
- Support Vector Machine
- Gradient Boosting
- GridSearchCV
- SelectKBest

Web Development

- HTML
- CSS
- Flask

Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

---


Running the Application

Run the Flask application:

python app.py

After starting the application, open the local Flask URL shown in the terminal in your web browser.

---

Project Workflow

Dataset
   ↓
Data Understanding
   ↓
Exploratory Data Analysis
   ↓
Data Preprocessing
   ↓
Feature Encoding & Scaling
   ↓
Feature Selection
   ↓
Model Training
   ↓
Model Comparison
   ↓
Hyperparameter Tuning
   ↓
Final Model Selection
   ↓
Model Evaluation
   ↓
Flask Deployment
   ↓
Customer Prediction

---

Key Findings

- The dataset contains a significant class imbalance.
- Customer and campaign-related features provide useful information for predicting subscription behavior.
- Numerical features contain skewness and outliers that require investigation.
- "pdays = -1" represents customers who were not previously contacted.
- Different classification algorithms produced different ROC-AUC performances.
- Gradient Boosting achieved the highest ROC-AUC among the compared models.
- The trained model can be integrated into a web application for interactive prediction.

---

Future Improvements

Possible future improvements include:

- Handling class imbalance using techniques such as SMOTE or class weighting.
- Testing additional boosting algorithms such as XGBoost, LightGBM, or CatBoost.
- Performing more extensive hyperparameter optimization.
- Adding additional evaluation metrics such as Precision, Recall, F1-score, and PR-AUC.
- Improving the user interface of the Flask application.
- Deploying the application to a cloud platform.
- Adding model explainability using techniques such as SHAP.

---

Conclusion

This project demonstrates an end-to-end machine learning approach for predicting customer responses to bank marketing campaigns.

Multiple classification algorithms were trained and compared, with Gradient Boosting achieving the best ROC-AUC score of 90.48% among the evaluated models.

The final model was integrated into a Flask web application, providing an interactive interface for generating customer subscription predictions and probabilities.

The project demonstrates practical skills in Python, data preprocessing, exploratory data analysis, feature engineering, feature selection, machine learning, model evaluation, hyperparameter tuning, and Flask deployment.
<img width="1816" height="900" alt="Screenshot 2026-10-08 053242" src="https://github.com/user-attachments/assets/97f72250-8352-4e90-b70b-26fbae6d6c36" />
<img width="1828" height="905" alt="Screenshot 2026-10-08 053325" src="https://github.com/user-attachments/assets/4dfbfc8b-8e7e-4659-a589-3ef30eb856b4" />
<img width="1821" height="662" alt="Screenshot 2026-10-08 053357" src="https://github.com/user-attachments/assets/12ec8fed-89c9-4687-9628-a3b47bb3a229" />
