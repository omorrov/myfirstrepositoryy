q=str(input('введите слова через пробел'))
w=q.split()
w.sort(key=len)
print(w)