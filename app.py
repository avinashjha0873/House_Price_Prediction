from flask import Flask, render_template, request
import joblib
app = Flask(__name__)


def predict(data):
    model = joblib.load("D:\Python\House_Price_Prediction\models\model.joblib")
    response = model.predict(data)
    return response

@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form:
            try:
                input_dict = dict(request.form).values()
                data = [list(map(float, input_dict))]
                print(data)
                response = predict(data)
                return render_template('base.html', response = response)
            except Exception as e:
                print(e)
                error = {"error": "Something! went! wrong"}
                return render_template("404.html", error = error)
    else:
        return render_template("base.html")

if __name__== "__main__":
    app.run(debug=True)

