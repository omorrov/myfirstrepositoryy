# tekst=input('Пожалуйста введите текст:')
# list1=list(tekst)
# print(list1)
# upperletters=0
# lowerletters=0
# for i in list1:
#     if i.islower():
#         lowerletters+=1
#     elif i.isupper():
#         upperletters+=1
# total=len(list1)
# print(upperletters)
# print(lowerletters)
# print(total)
# a=100*upperletters/total
# b=100*lowerletters/total
# itog=a+b
# print(str(a)+'%') 
# print(str(b)+'%')
# print(itog)


# q=int(input(задайте целое число: ))
# o=0
# if 0<=o:
#     print(1)
# elif 0>=o:
#     print(-1)
# elif 0==o:
#     print(0)



# q=int(input('введите число'))
# list1=list(range(1,q))
# e=1
# for i in list1:
#     e*=i
# print(e)

input_str = []
temp = {}
 
for i in range(int(input("Введите количество строк: "))):
    input_str.append(input("Введите строку: "))
 
input_str.sort()
 
for i in input_str:
    if len(i) in temp.keys():
        temp[len(i)] = temp[len(i)] + f", {i}"
    else:
        temp[len(i)] = i
 
keys = list(temp.keys())
keys.sort()
 
for i in range(len(keys)):
    for j in temp[keys[i]].split(", "):
        print(j)







