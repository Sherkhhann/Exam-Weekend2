# 4:
#     Given a list of numbers and the index of the element in the list k. Remove an element with index k.

#     Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k.
#     Input data
#     7 6 5 4 3 2 1
#     2

#     Output
#     7 6 4 3 2 1 

list_of_num=input().split()
k=int(input())
list_of_num.pop(k)
for i in list_of_num:
	print(i, end=" ")
