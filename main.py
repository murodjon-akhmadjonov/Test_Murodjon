# polymorphism
# incapsulation in OOP 

class User:
    def __init__(self, name ,age):
        self.name = name
        self.age = age


    def show_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

user = User("john",30)
user.show_info()


class Admin(User):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def show_info(self):
        super().show_info()
        print(f"Role: {self.role}")

admin = Admin(f"John", 30 , "Admin")
admin.show_info()