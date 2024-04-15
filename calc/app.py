from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_route():
  a = int(request.args.get("a", 0)) # default to 0
  b = int(request.args.get("b", 0))
  result = add(a,b)
  return str(result)

@app.route("/sub")
def sub_route():
  a = int(request.args.get("a", 0)) # default to 0
  b = int(request.args.get("b", 0))
  result = sub(a,b)
  return str(result)

@app.route("/mult")
def mult_route():
  a = int(request.args.get("a", 1)) # default to 1
  b = int(request.args.get("b", 1))
  result = mult(a,b)
  return str(result)

@app.route("/div")
def div_route():
  a = int(request.args.get("a", 1)) # default to 1 so not dividing by 0
  b = int(request.args.get("b", 1))
  result = div(a,b)
  return str(result)

operators = {
  "add": add,
  "sub": sub,
  "mult": mult,
  "div": div
}

@app.route("/math/<operation>")
def operate(operation):
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = operators[operation](a,b)

  return str(result)