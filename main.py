from models import Work
from storage import load_data, save_data, load_bonus, save_bonus, load_fine, save_fine
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
            worker_object = Work(
                        worker['new_id'],
                        worker['name'],
                        worker['last_name'],
                        worker['age'],
                        worker['post'],
                        worker['salary']
                    )
            worker_object.get_info()
            
        if choice == 2:
            data = load_data()
            employee = input('Введите id или имя/фамилию сотрудника: ')
            found = False
            for user in data:
                if (
                    str(user['new_id']) == employee
                    or user['name'] == employee
                    or user['last_name'] == employee
                ):
                    found = True
                    worker = Work(
                        user['new_id'],
                        user['name'],
                        user['last_name'],
                        user['age'],
                        user['post'],
                        user['salary']
                    )
                    worker.get_info()
                    
                    while True:
                        print(f'Выберите действие: ')
                        print(f'1. Добавить бонус')
                        print(f'2. Добавить штраф')
                        print(f'3. Узнать причину бонуса(ов)')
                        print(f'4. Узначить причину штрафа(ов)')
                        print(f'5. Посмотреть финальную выплату')
                        print(f'6. Выйти')
                        action = int(input('Выберите желаемое действие: '))
                        
                        if action == 1:
                            bonus_sis = load_bonus()
                            reason = input('Напишите причину бонуса: ')
                            bonus = int(input('Введите сумму бонуса: '))
                            user['salary'] += bonus
                            save_data(data)
                            info_bonus = {
                                'worker_id': user['new_id'],
                                'reason': reason,
                                'bonus': bonus
                            }
                            bonus_sis.append(info_bonus)
                            save_bonus(bonus_sis)
                            print('Бонус успешно добавлен.')
                            
                        if action == 2:
                            fine_sis = load_fine()
                            reason = input('Напишите причину штрафа: ')
                            fine = int(input('Введите сумму штрафа: '))
                            user['salary'] -= fine
                            save_data(data)
                            info_fine = {
                                'worker_id': user['new_id'],
                                'reason': reason,
                                'fine': fine
                            }
                            fine_sis.append(info_fine)
                            save_fine(fine_sis)
                            print('Штраф успешно добавлен.')
                        
                        if action == 3:
                            bonuses = load_bonus()
                            for bonus in bonuses:
                                if bonus['worker_id'] == user['new_id']:
                                    print(f'ID: {bonus['worker_id']} | Причина: {bonus['reason']} | Сумма: {bonus['bonus']}')
                                    
                        if action == 4:
                            fines = load_fine()
                            for fine in fines:
                                if fine['worker_id'] == user['new_id']:
                                    print(f'ID: {fine['worker_id']} | Причина: {fine['reason']} | Сумма: {fine['fine']}')
                                    
                        if action == 5:
                            data = load_data()
                            for user in data:
                                if worker.id == user['new_id']:
                                    print(f'Финальная выплата сотруднику {user['name']} {user['last_name']}: {user['salary']}')
                        
                        if action == 6:
                            break
                    break
                    
            if not found:
                print('Сотрудник не найден.')
                
        if choice == 3:
            data = load_data()
            for user in data:
                print(f'ID: {user['new_id']} | Имя: {user['name']} | Фамилия: {user['last_name']} | Возраст: {user['age']} | Должность: {user['post']} | Зарплата: {user['salary']}')
        
        if choice == 4:
            data = load_data()
            remove_user = input('Введите ID или имя сотрудника, кого хотите удалить: ')
            found = False
            for user in data:
                if (
                    str(user['new_id']) == remove_user
                    or user['name'] == remove_user
                ):
                    found = True
                    data.remove(user)
                    save_data(data)
                    print('Сотрудник удален.')
                    break
        
        if choice == 5:
            print('Программа завершена.')
            break
        
    except ValueError:
        print ('Произошла ошибка! Проверьте данные, которые вводите.')
        