#/usr/bin/python

class school_member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "Initializing school member:", self.name

    def tell(self):
        '''Tell my details.'''
        print "Name:%s, Age:%d" % (self.name, self.age)

class teacher(school_member):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        school_member.__init__(self, name, age)
        self.salary = salary
        print "Initializing teacher:", self.name

    def tell(self):
        school_member.tell(self)
        print "Salary: %d" % self.salary


class student(school_member):
    '''Represents a student.'''
    def __init__(self, name, age, score):
        school_member.__init__(self, name, age)
        self.score = score
        print "Initializing student:", self.name

    def tell(self):
        school_member.tell(self)
        print "Score: %d" % self.score

t = teacher("Mrs. Chen", 43, 8000)
s = student("Zongsen", 28, 88)

members = [t, s]
for member in members:
    member.tell()

