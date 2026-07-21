class animal():
	def __init__(self,name):
		self.name = name
		
	def bark(self):
		print(f"{self.name} is barking continuously !")
		print("best dog")
		print("good dog")
		#more lines........
		
		
class dog(animal):
	def bark(self):
		super().bark()
		print(f"{self.name} can also speak !")
		

class cat(animal):
	pass
	
d = dog("rex")
c = cat("kitty")

print(d.bark())
print(c.bark())
