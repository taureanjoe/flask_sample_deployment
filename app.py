from flask import Flask, render_template, request
import areas as a 


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        area= request.form["plot_area"]
        areas_prediction = a.price_predict(area)
        #print(areas_prediction)
        ap = areas_prediction
    return render_template("index.html", my_price=ap)



# @app.route("/sub", methods =['POST'])
# def submit():
#     if request.method == "POST":
#         name = request.form["plot_area"]

#     return render_template("submit.html", n=name)


if __name__ == "__main__":
    app.run(debug=True)

