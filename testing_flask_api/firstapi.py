from flask import Flask,request
app=Flask(__name__)
@app.route("/")
def testing_name():
    x="hello there i am testing the server"
    return x
@app.route("/greetings")
def greet():
    name= request.args.get("name","Yvan")
    return f"hi there {name}, how are you"
@app.route("/status")
def status():
    return "server running smoothy"
@app.route("/square")
def squareroute():
 x=5
 return f"the squre of {x} is 25"
if __name__=="__main__":
    app.run(debug=True )    