from model.utils import flowerModel
from flask import Flask,jsonify,render_template,request
import config


app = Flask(__name__)

@app.route("/")

def hello_flask():
    print("We are in Flask API")
    return render_template("index.html")
    
@app.route("/flower_pred",methods=["POST"])

def get_predicted():



    SepalLengthCm= eval(request.form.get("SepalLengthCm"))
    SepalWidthCm = eval(request.form.get("SepalWidthCm"))
    PetalLengthCm= eval(request.form.get("PetalLengthCm"))
    PetalWidthCm = eval(request.form.get("PetalWidthCm")) 

    print("SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm\n" , SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)

    Obj=flowerModel(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    result1= Obj.get_flower_prediction()
   
    return render_template("index.html",prediction=result1) 


if __name__ == "__main__":
    app.run(host="0.0.0.0",port = config.PORT_NUMBER, debug=True)