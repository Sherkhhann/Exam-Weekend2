# 6:
#     Cycle the elements of the list to the right (A[0] goes to place A[1], A[1] to place A[2], ..., last element goes to place A[0]).

#     Циклически сдвиньте элементы списка вправо (A[0] переходит на место A[1], A[1] на место A[2], ..., последний элемент переходит на место A[0]).
#     Input data
#     1 2 3 4 5

#     Output
#     5 1 2 3 4 

a=input().split()
n=len(a)
i=n-1
num=a[-1]
while i>0:
	a[i]=a[i-1]
	i-=1
a[0]=num
for j in a:
	print(j, end=" ")
