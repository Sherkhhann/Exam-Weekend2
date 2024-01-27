# 3:
#     Print all exact squares of natural numbers not exceeding a given number N.

#     Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.
#     Input data
#     15

#     Output
#     1 4 9

a=int(input())
i=0
while i<a:
	if (a**0.5)%1==0:
		print(a, end=" ")
	a-=1