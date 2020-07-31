#Поиск минимума в списке
s = '5 8 4 3 5 7'
lst = [int(i) for i in s.split()]
minValue = lst[0]
for i in lst:
    if i < minValue:
        minValue = i
print(minValue)