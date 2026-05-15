class Work:
    def __init__(self, id, name, last_name, age, post, salary):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.age = age
        self.post = post
        self.salary = salary
        
    def get_info(self):
        print(f'ID: {self.id} | Сотрудник: {self.name} {self.last_name} | Возраст: {self.age} | Должность: {self.post} | Зарпалата: {self.salary} ')
        
    def bonus_sistem(self, bonus):
        self.salary += bonus
        print(f'Зарплата с учетом бонуса: {self.salary}')
        