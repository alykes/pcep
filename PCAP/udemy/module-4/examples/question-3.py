class MyEx(Exception):
  def __init__(self, msg):
    Exception.__init__(self, msg+msg)
    self.args = (msg + ' This will print because it prints a the tuple in args',)
 
try:
  raise MyEx('wrong!')
except Exception as e:
  print(e)

##########################

class MyEx2(Exception):
  def __init__(self, msg):
    Exception.__init__(self, msg+msg)                                       # This message will print, which will be 'wrong!wrong!'
    #self.args = (msg + ' args is what is used to print the message',)      # args is used to print the message, but if it isn't defined, then it will print what was send to the constructor
 
try:
  raise MyEx2('wrong!')
except Exception as e:
  print(e)