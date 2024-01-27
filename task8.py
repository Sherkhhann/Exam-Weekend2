# 8:
#     Write a Python program to find the maximum and minimum product of pairs of tuples within a given list.

#     Напишите программу на Python, чтобы найти максимальное и минимальное произведение пар кортежей в заданном списке.

#     The original list, tuple : [(2, 7), (2, 6), (1, 8), (4, 9)]

#     Maximum and minimum product from the pairs of the said tuple of list: Максимальное и минимальное произведение пар   указанного кортежа списка:

#     (36, 8)

a=[(2, 7), (2, 6), (1, 8), (4, 9)]
s=1
b=[]
for i in a:
	for j in i:
		j=j*1
	b.append(s)
print(b)