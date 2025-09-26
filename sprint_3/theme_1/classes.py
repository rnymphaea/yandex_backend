class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender

employee1 = Employee('Robert', 'Cruso', 'м')
employee1.vacation_days = 30

employee2 = Employee('Devin', 'Grayson', 'м')


print(f"Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {employee1.gender}, Отпускных дней в году: {employee1.vacation_days}.")

Employee.vacation_days = 32
print(f"Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, Пол: {employee2.gender}, Отпускных дней в году: {employee2.vacation_days}.")
