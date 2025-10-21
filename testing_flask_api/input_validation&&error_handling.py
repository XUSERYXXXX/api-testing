from flask import Flask,request,jsonify
#create the instance app
app=Flask(__name__)
#create the routes and logic
@app.route("/")
def root():
    return "this is the root page"
@app.route("/validation")
def addition():
    numb_1=request.args.get("numb_1")
    numb_2=request.args.get("numb_2")
    if numb_1 is None or numb_2 is None:
        return jsonify(
            {
              "error_message":"please input numbers to perfom the operation"
            } 
        ),400
    
    try:
        numb_1=int(numb_1)
        numb_2=int(numb_2)
        summation=numb_1+numb_2
    except ValueError:
        return jsonify(
            {
                "error":"both numbers must be integers "
            }
        ),400    
    result={
        "number_1":numb_1,
        "number_2":numb_2,
        "summation":summation
        }
    return jsonify(result)
#challenge 3
@app.route("/devide")
def devision():
    div_numb1=request.args.get("number_1")
    div_numb2=request.args.get("number_2")
    #checking if the numbers are there
    if div_numb1 is None or div_numb2 is None:
        return jsonify(
            {
                "error":"there must numbers "
            }
        ),400
   #coverting into integers
    try:
        div_numb1=int(div_numb1)
        div_numb2=int(div_numb2)
    except ValueError:
        return jsonify(
            {
                "error":"parameters must be numbers"
            }
        ),400
    if div_numb2==0:
        return jsonify(
            {
                "error":"the second number can not be = 0"
            }
        ),400
    
    division=div_numb1/div_numb2
    division=int(division)

    final_result={
      "number_1":div_numb1,
      "number_2":div_numb2,
      "division":division
                 }
    return jsonify(final_result)
if __name__=="__main__":
    app.run(debug=True)