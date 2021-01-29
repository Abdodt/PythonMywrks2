"""
class Adders:
    def __init__(self,num1):
        self.num1 = num1
        
    def __add__(self,other):
        return self.num1 + other.num1
    
a =Adders(5)
b =Adders(11)

print(a+b)
"""

class Day(object):
    def __init__(self, visits, contacts):
        self.visits = visits
        self.contacts = contacts

    def __add__(self, other):
        total_visits = self.visits + other.visits
        total_contacts = self.contacts + other.contacts
        return Day(total_visits, total_contacts)
"""
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
"""
def __str__(self):
        return "Visits: %i, Contacts: %i" % (self.visits, self.contacts)

day1 = Day(10, 1)
day2 = Day(20, 2)
print day1
# Visits: 10, Contacts: 1
print day2
# Visits: 20, Contacts: 2

day3 = day1 + day2
print day3
# Visits: 30, Contacts: 3

day4 = sum([day1, day2, day3])
print day4
# Visits: 60, Contacts: 6


""""Dunder or magic methods in Python are the methods having two prefix and suffix 
underscores in the method name. Dunder here means “Double Under (Underscores)”. 
These are commonly used for operator overloading. 
Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

The __init__ method for initialization is invoked without any call, when an instance of a class is created,
 like constructors in certain other programming languages such as C++, Java, C#, PHP etc. 
 These methods are the reason we can add two strings with ‘+’ operator without any explicit typecasting.

"""