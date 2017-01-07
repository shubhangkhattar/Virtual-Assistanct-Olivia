import oliviaTTS as ot

def calculate (data):
    
    try:
              data = data.split(" ",1)
              eqn = data[1]
              print("equation before evaluation : " + eqn)
              print(eqn)
              if "multiply" in eqn:
                   print("here")
                   eqn=eqn.replace("multiply","*")
              if "divide" in eqn:
                   eqn=eqn.replace("divide","/")
              if "subtract" in eqn:
                   eqn=eqn.replace("subtract","-")
              if "add" in eqn:
                   eqn=eqn.replace("add","+")
              print("equation after evaluation" + eqn)    
              print("solving " + eqn)
              ans=eval(eqn)
              print("answer is "+str(ans))
              ot.speak("answer is " + str(ans))
              data=""
              
    except:
                print("incorrect equation")
                ot.speak("please repeat the equation")
