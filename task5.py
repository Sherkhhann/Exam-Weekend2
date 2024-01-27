# 5:
#     In the list, all elements are different. Swap the minimum and maximum elements of this list.
    
#     В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
#     Input data
#     3 4 5 2 1

#     Output
#     3 4 1 2 5 

a=input().split()
maxx=-9999
minn=9999
n=len(a)
i=0
while int(i) < n:
	if int(a[i])<int(minn):
		minn = a[i]
		index_minn=int(i)
	i+=1
i=0
while int(i) < n:
	if int(a[i]) > int(maxx):
		maxx = a[i]
		index_maxx=int(i)
	i+=1
a[index_minn]=maxx
a[index_maxx]=minn
b=list(a)
for j in b:
	print(j, end=" ")