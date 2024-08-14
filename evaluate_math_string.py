# Following Code will evaluate the math equation written in a string

def evaluate(expression):
  for equation in expression:
    if len(equation)>1 and len(equation)<=100:
      equation=equation.replace("plus","+")
      equation=equation.replace("minus","-")
      equation=equation.replace("times","*")
      equation=equation.replace("divided by","/")
      equation=equation.replace(" ","")
      #print(expression)
      #expression1=int(expression)
      result = eval(equation)
      print(float(result))

evaluate(["5 plus ( 3 times 2 )", "2 plus ( 5 times 6 )"])
