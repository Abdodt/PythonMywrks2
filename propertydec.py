class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    """ If we had only made an email """

    # @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    """@fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
"""

emp_1 = Employee('John', 'Smith')
emp_1.first = "Jacob"
emp_1.fullname = "Corey Schafer"
emp_1.last = "Shwarzenegger"

print(emp_1.first)
print(emp_1.email) #if we are not using @property then we'll need to call email as a function like email() and not just email.
print(emp_1.fullname)

del emp_1.fullname

"""@property decorator is a built-in decorator in Python which is helpful in defining the properties effortlessly without 
manually calling the inbuilt function property().
 Which is used to return the property attributes of a class from the stated getter, setter and deleter as parameters

PROPERTY  decarotor allows us to define a method(def function) but we can access it like an attribute.

It's applications
By using property() method, we can modify our class and implement the value constraint without any change r
equired to the client code. So that the implementation is backward compatible.

"""

"""
 class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname"""