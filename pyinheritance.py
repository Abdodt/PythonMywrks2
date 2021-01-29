# Python code to demonstrate how parent constructors 
# are called. 

# parent class 
#Simple prgm

# class Person( object ):	 

# 		# __init__ is known as the constructor		 
# 		def __init__(self, name, idnumber): 
# 				self.name = name 
# 				self.idnumber = idnumber 
# 		def display(self): 
# 				print(self.name) 
# 				print(self.idnumber) 

# # child class 
# class Employee( Person ):		 
# 		def __init__(self, name, idnumber, salary, post): 
# 				self.salary = salary 
# 				self.post = post 

# 				# invoking the __init__ of the parent class 
# 				Person.__init__(self, name, idnumber) 

				
# # creation of an object variable or an instance 
# a = Employee('Rahul', 886012, 200000, "Intern")	 

# # calling a function of the class Person using its instance 
# a.display() 



class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # def add_emp(self, emp):
    #     if emp not in self.employees:
    #         self.employees.append(emp)

    # def remove_emp(self, emp):
    #     if emp in self.employees:
    #         self.employees.remove(emp)

    # def print_emps(self):
    #     for emp in self.employees:
    #         print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_2)

# mgr_1.print_emps()