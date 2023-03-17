# new line added to commit

from flask import Flask,request,render_template
import pickle

with open("model.pkl","rb") as file:
    model=pickle.load(file)

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/salary_pred",methods=["POST"])
def salary_pred():
    data=request.form
    years_exp=float(data["html_years_exp"])

    prediction=model.predict([[years_exp]])

    return render_template("index.html",salary=prediction)


if __name__=="__main__":
    app.run()

