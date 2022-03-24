#HERARCHICAL INHERITANCE
class student():
	def getdata(self):
		self.name=input("enter the name :")
		self.usn=input("enter the usn :")
		self.age=int(input("enter the age :"))
class pgstudent(student):
	def pggetdata(self):
		super().getdata()
		self.sem=int(input("enter the sem :"))
		self.fees=int(input("enter the fees :"))
		self.stipend=int(input("enter the stipend :"))
	def display(self):
		print("NAME :",self.name)
		print("USN :",self.usn)
		print("AGE :",self.age)
		print("SEM :",self.sem)
		print("FEES :",self.fees)
		print("STIPEND :",self.stipend)
class ugstudent(student):
        def uggetdata(self):
                super().getdata()
                self.sem=int(input("enter the sem :"))
                self.fees=int(input("enter the fees :"))
                self.stipend=int(input("enter the stipend :"))
        def display(self):
                print("NAME :",self.name)
                print("USN :",self.usn)
                print("AGE :",self.age) 
                print("SEM :",self.sem)
                print("FEES :",self.fees)
                print("STIPEND :",self.stipend)
pg={}
ug={}
n=int(input("enter the number of students :"))
for i in range (n):
	print(" 1--enter pgstudent detials :")
	print("2--enter ugstudent details :")
	ch=int(input("select choice "))
	if ch==1:
		ob1=pgstudent()
		ob1.pggetdata()
		pg[ob1.name]=ob1.__dict__
	elif ch==2:
		ob2=ugstudent()
		ob2.uggetdata()
		ug[ob2.name]=ob2.__dict__
print(ug)
print(pg)

