from random import randrange

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
      return "Added grade with score %s" % grade.score
    
  def get_average(self, score):
      return sum(self.grades) / len(self.grades)
  
      
class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score

  def __repr__(self):
    if self.score > 80:
      return "A"
    elif self.score > 75:
      return "B"
    elif self.score > 70:
      return "C"
    elif self.score > 65:
      return "D"
    else:
      return "F"

  def is_passing(self):
    if self.score < self.minimum_passing:
      return 'You did not pass this subject'
    else:
      return ' You aced it!'
    
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
print(pieter.add_grade(Grade(100)))

for x in range(4):
  pieter.add_grade(Grade(randrange(50,100)))

for grade in pieter.grades:
  print(grade, end=', ')