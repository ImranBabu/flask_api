from flask import Flask,make_response,request

app = Flask(__name__)

@app.route("/")
def home():
    response = make_response({"message":"This is sample API"})
    response.set_cookie("name","Imran")
    return response

@app.route("/get_name",methods=["GET"])
def get_name():
    saved_name = request.cookies.get('name')
    response = make_response({"saved_name":saved_name})
    return response

@app.route("/set_name",methods=["POST"])
def set_name():
    data = request.json
    response = make_response({"message":"Name has been set"})
    response.set_cookie("name",data["name"])
    return response

if __name__ == "__main__":
    app.run("0.0.0.0")