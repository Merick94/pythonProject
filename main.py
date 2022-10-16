#exam_2_6 Даны 2 списка чисел. В них могут быть
# одинаковые числа. Посчитайте, сколько в списках одинаковых чисел
sp1 = input().split()
sp2 = input().split()
count = 0
for i in sp1:
    if i in sp2:
        count +=1
print(count)