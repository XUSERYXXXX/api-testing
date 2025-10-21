#--->challenge is to creat a one end-point  for calcutions
#--->importing the nessary libraries
from flask import Flask,jsonify,request
#--->creating the instances of the application
app= Flask(__name__)
#routes 
@app.route("/")
def welcome():
 return "welcome to root page"
@app.route("/calculations",methods=["POST"])
def calculation():
 data= request.get_json()#getting data from the client(postman or oher)
 operation=data.get("operation")
 try:
  numb1=int(data["numb1"])
  numb2=int(data["numb2"])
 except ValueError:
  return jsonify(
   {
    "error":"both values must be numbers"
   }
  ),400
 except KeyError:
  return jsonify(
   {
    "error":"both values must be entered"
   }
  ),400
 #what type of operation to execute
 if operation=="addition":
  result=numb1+numb2
  return jsonify(
   {
    "operations":operation,
    "numb1":numb1,
    "numb2":numb2,
    "result":result
   }
  )
 if operation=="subtraction":
  result=numb1-numb2
  return jsonify(
   {
    "operations":operation,
    "numb1":numb1,
    "numb2":numb2,
    "result":result
   }
  )
 if operation=="multiplication":
  result=numb1*numb2
  return jsonify(
   {
    "operations":operation,
    "numb1":numb1,
    "numb2":numb2,
    "result":result
   }
  )
 if operation=="division":
  try:
   result=numb1/numb2
  except ValueError:
   return jsonify(
    {
     "error":"the second number can not be 0"
    }
   ),400 
  return jsonify(
   {
    "operations":operation,
    "numb1":numb1,
    "numb2":numb2,
    "result":result
   }
  )
 
if __name__ == "__main__":
  app.run(debug=True)
 


 


