from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained machine learning pipeline
model = joblib.load("model/bank_marketing_final_pipeline.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get data from the HTML form
    data = {
        "age": int(request.form["age"]),
        "job": request.form["job"],
        "marital": request.form["marital"],
        "education": request.form["education"],
        "default": request.form["default"],
        "balance": int(request.form["balance"]),
        "housing": request.form["housing"],
        "loan": request.form["loan"],
        "contact": request.form["contact"],
        "day": int(request.form["day"]),
        "month": request.form["month"],
        "duration": int(request.form["duration"]),
        "campaign": int(request.form["campaign"]),
        "pdays": int(request.form["pdays"]),
        "previous": int(request.form["previous"]),
        "poutcome": request.form["poutcome"]
    }

    # Convert the input into a DataFrame
    input_data = pd.DataFrame([data])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Get probability of subscription
    probability = model.predict_proba(input_data)[0][1]

    # Convert prediction into readable text
    if prediction == 1:
        result = "The customer is likely to subscribe to a term deposit."
    else:
        result = "The customer is unlikely to subscribe to a term deposit."

    return render_template(
        "index.html",
        prediction=result,
        probability=round(probability * 100, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)