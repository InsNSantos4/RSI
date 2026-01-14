class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
  def envelhece(self,anos):
    self.age = self.age + anos

p1 = Person("John", 36)
print(p1.age)
p1.age=15
print(p1.age)
p1.myfunc()
p1.envelhece(4)
print(p1.age)

p1.sex='M'
print(p1.sex)

p1.age+=10
print(p1.age)