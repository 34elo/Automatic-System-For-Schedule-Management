from database_functions.schedule_functions import get_schedule, get_my_schedule

path1 = '../../data/users_data.sqlite'
path2 = '../../data/schedule.sqlite'

print('*** Test get_schedule ***')
print(get_schedule('Рыленкова_18', path2))
print(get_schedule('Багратиона_16', path2))
print(get_schedule('Крупской_42', path2), '\n')

print('*** Test get_my_schedule ***')
print(get_my_schedule('denis_shumilov', path1, path2))
print(get_my_schedule('serjanchik', path1, path2))
print(get_my_schedule('test_username', path1, path2))