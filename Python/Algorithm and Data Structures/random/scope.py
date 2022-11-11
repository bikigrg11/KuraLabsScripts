def myfunc():
    
  x = 300
  def myinnerfunc():
    global x 
    x = 200
    print(x)
  
  myinnerfunc()

myfunc()

print(x)
