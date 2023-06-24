class Employee:
    def __init__(self, name, age, department, is_manger, rating):
        self.name = name
        self.age = age
        self.department = department
        self.is_manger = is_manger
        self.rating = rating #rating from 1-5
    
    def is_excellent(self):
        return True if self.rating >= 4.5 else False