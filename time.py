q=int(input('введите час :'))
w=int(input('введите минуту :'))
e=int(input('введите секунду :'))
r=int(input('введите конечный час :'))
t=int(input('введите конечную минуту :'))
y=int(input('введите конечную секунду :'))
a=r-q
s=t-w
d=y-e
v=a*60*60
m=t*60
u=v+m
i=y-e
k=u+i
print('прошло всего времени:'+str(a)+':'+str(s)+':'+str(d))
print('Прошло секунд:'+str(k))
