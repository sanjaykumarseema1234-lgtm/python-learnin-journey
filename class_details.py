class student:
	def __init__(self,name,age,subject,marks):
		self.name = name
		self.age = age
		self.subject = subject
		self.marks = marks
		
s1 = student("sanjay",18,"python",95)
s2 = student("rahul",19,"python",99)

print(f"{s1.name} , {s1.age} , {s1.subject} , {s1.marks}")
print(f"{s2.name} , {s2.age} , {s2.subject} , {s2.marks}")

print("only students for practial experince of oops !")
