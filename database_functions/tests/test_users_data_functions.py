from database_functions.users_data_functions import (get_admin_names, get_admin_contact,
                                                     get_employee_contact, get_full_name_by_username,
                                                     get_all_chat_ids)

path1 = '../../data/users_data.sqlite'
path2 = '../../data/schedule.sqlite'

print('*** Test get_admin_names ***')
print(get_admin_names(path1), '\n')

print('*** Test get_admin_contact ***')
print(get_admin_contact('Максим Максимович Максимов', path1))
print(get_admin_contact('Петр Петрович Петров', path1))
print(get_admin_contact('Василий Васильевич Васильев', path1))
print(get_admin_contact('Максим Максимович Достоевский', path1), '\n')

print('*** Test get_employee_contact ***')
print(get_employee_contact('Петр Максимович Астафьев', path1))
print(get_employee_contact('Максим Петрович Астафьев', path1))
print(get_employee_contact('Георгий Андреевич Смирнов', path1))
print(get_employee_contact('Дмитрий Дмитриевич Соловьев', path1))
print(get_employee_contact('Артем Витальевич Цветков', path1))
print(get_employee_contact('Виталий Иванович Тургенев', path1), '\n')

print('*** Test get_full_name_by_username ***')
print(get_full_name_by_username('serjanchik', path1))
print(get_full_name_by_username('denis_shumilov', path1))
print(get_full_name_by_username('test_username', path1), '\n')

print('*** Test get_all_chat_ids ***')
print(get_all_chat_ids(path1))
