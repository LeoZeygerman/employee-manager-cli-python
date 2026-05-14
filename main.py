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
            worker = {
                name: 'name',
                last_name: 'last_name',
                age: 'age',
                post: 'post',
                salary: 'salary'
            }
            data.append(worker)
            save_data(data)
        
    except ValueError:
        print ('Произошла ошибка! Проверьте данные, которые вводите.')
        