from models import Work
from storage import load_data, save_data
while True:
    try:
        print('Варианты дейтсвий: ')
        print('1. Добавить сотрудника')
        print('2. Найти сотрудника')
        print('3. Список всех сотрудников')
        print('4. Удалить сотрудника')
        print('5. Выйти')
        choice = int(input('Выберите желаемое действие: '))
        
        if choice == 1:
            data = load_data()
            name = input('Введите имя сотрудника: ')
            last_name = input('Введите фамилию сотрудника: ')
            age = input('Введите возраст сотрудника: ')
            post = input('Введите должность сотрудника: ')
            salary = int(input('Введите зарплату сотрудника: '))
            if len(data) == 0:
                new_id = 1
            else:
                new_id = data[-1]['new_id'] + 1
            worker = {
                'new_id': new_id,
                'name': name,
                'last_name': last_name,
                'age': age,
                'post': post,
                'salary': salary
            }
            data.append(worker)
            save_data(data)
            
        if choice == 2:
            data = load_data()
            employee = input('Введите id или имя/фамилию сотрудника: ')
            for user in data:
                if (
                    str(user['new_id']) == employee
                    or user['name'] == employee
                    or user['last_name'] == employee
                    or user['name'], user['last_name'] == employee
                ):
                    worker = Work(
                        user['new_id'],
                        user['name'],
                        user['last_name'],
                        user['age'],
                        user['post'],
                        user['salary']
                    )
                    worker.get_info()
                else:
                    print(f'Сотрудник не найден.')
        
    except ValueError:
        print ('Произошла ошибка! Проверьте данные, которые вводите.')
        