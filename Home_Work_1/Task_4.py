# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Enter the first value: '))
m = int(input('Enter the second value: '))
k = int(input('Enter the third value: '))

if k < m*n and (k % m == 0 or k % n == 0):
    print('-> yes')
else:
    print('-> no')