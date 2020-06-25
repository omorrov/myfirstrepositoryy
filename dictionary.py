# for x in range(1,12):
#     print(x, end='-')
#     print('q')
#     print('qw')

# alien_0={'color': 'green','points':5}
# print(alien_0['color'])
# print(alien_0['points'])

# points=100
# alien_0={'color': 'green','points':5}   добавляем очки из словаря
# points+=alien_0['points']
# print(points)

# alien_0={'color': 'green','points':5}
# print('we killed '+alien_0['color'].upper()+ ' alien. we got 5 points')


# alien_0={'color': 'green','points':5}
# print(alien_0)
# alien_0['x.position']=0
# alien_0['y.position']=25    #добавление новых пар ключей значения в наш словарь
# alien_0['color']='red'  #изменение ключа на новый
# print(alien_0)

# alien_0={'x_position':150,'y_position':25,'speed': 'medium'}
# if alien_0['speed']=='slow':
#     x_increment=2
# elif alien_0['speed']=='medium':
#     x_increment=5
# else:
#     x_increment=10
#     print('speed wz x, equal to:', x_increment)
#     alien_0['x_position']=alien_0['x_position']+x_increment
#     print(alien_0['x_position'])

alien_0={'x_position':150,'y_position':25,'speed': 'slow'}
del alien_0['speed']
print(alien_0)


