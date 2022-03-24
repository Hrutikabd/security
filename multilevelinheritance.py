#Multilevle inheritance
class student:
	def getdata(self):
		self.usn=input("enter the usn:")
		self.name=input("enter the name:")
		self.age=int(input("enter the age :"))
class derived1(student):
	def getmarks(self):
		super().getdata()
		self.s1=int(input("enter subject1 marks :"))
		self.s2=int(input("enter subject2 marks :"))
		self.s3=int(input("enter subject3 marks :"))
		self.s4=int(input("enter subject4 marks :"))
		self.s5=int(input("enter subject5 marks :"))
		self.total=self.s1+self.s2+self.s3+self.s4+self.s5
		self.perc=self.total / 500 * 100
class derived2(derived1):
		def display(self):
			print("USN :",self.usn)
			print("NAME :",self.name)
			print("AGE :",self.age)
			print("TOTAL  :",self.total)
			print("percentage :",self.perc)
d={}
n=int(input("enter the number of students :"))
for i in range (n):
	d2=derived2()
	d2.getmarks()
	d[d2.name]=d2.__dict__
print(d) 
