from multipledispatch import dispatch 
class person:
        @dispatch()
        def hello():
                print("hello")
        @dispatch(str)
        def hello(name):
                print("your name i",name)
        @dispatch(int)
        def hello(age):
                print("your age is",age)
        @dispatch(str,int)
        def hello(name,age):
                print("your name is ",name,"your age is ",age)  
p1=person()
p1.hello()
p1.hello("abd")
p1.hello(34)
p1.hello("abd",34)


