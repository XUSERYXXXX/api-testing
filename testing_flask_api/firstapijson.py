from flask import Flask, request, jsonify
#creating the app instances 
app=Flask(__name__)
#creating routes
@app.get("/")
def home():
    return "this is the root page "
@app.route("/details")
def detailling():
    name=request.args.get("name","mr.nobody")
    age= request.args.get("age","unspecified")
    occupation=request.args.get("ocuppation","software engineer")
    
    response = {
        "name":name,
        "age":age,
        "occuppation":occupation
        }
    return jsonify(response)
@app.route("/status")
def status():
    statses=request.args.get("status","running")
    state={
        "stts":statses,
        "message":"the server is running smooth"
        }
    return jsonify(state)
@app.route("/add")
def addition():
     numb1= 1000
     numb2=2000
     sum=numb1+numb2
     summation={
         "number_1":numb1,
         "number_2":numb2,
         "the_sum":sum
         }
     return jsonify(summation)

if __name__=="__main__":
    app.run(debug=True)