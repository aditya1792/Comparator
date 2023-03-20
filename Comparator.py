'''
    Operator Overloading in python
'''

class Employee:
    def __init__(self, p):
        self.price = p
 
    def __lt__(self, other):
        return self.price < other.price
        
    def __gt__(self, other):
        if(self.price > other.price):
            return True
        else:
            return False

    def __le__(self, other):
        if(self.price <= other.price):
            return True
        else:
            return False
        
        
emp1 = Employee(100000)
emp2 = Employee(75000)

if(emp1 < emp2):
    print('\n emp1 is lesser ')
else:
    print('\n emp2 is lesser ')

    
if(emp1 > emp2):
    print('\n emp1 is greater ')
else:
    print('\n emp2 is greater ')


if(emp1 <= emp2):
    print('\n emp1 is lesser or equal ')
else:
    print('\n emp2 is lesser or equal')
