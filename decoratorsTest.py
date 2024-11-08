def say_hi(func):
    def wrapper(*args,**kwargs):
          print("HI")
          ret = func(*args,**kwargs)
          print("BYE")
          return ret
  
    return wrapper
 
 
def say_yo(func):
     def wrapper(*args,**kwargs):
         print('yo')
         ret = func(*args,**kwargs)
         return ret
     return wrapper
 
# 加载顺序是由下而上  实际上  func = say_hi(say_yo(func))
@say_hi   # func = say_hi(func)
@say_yo   # func = say_yo(func)
def func():
     print('hello world')
func()