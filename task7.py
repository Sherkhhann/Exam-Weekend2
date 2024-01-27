# 7:
#     Given a list of numbers. Count how many pairs of elements are in it that are equal to each other. It is believed that any two elements equal to each other form one pair that must be counted.

#     Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

#     Input data                Input data
#        1 2 3 2 3                1 1 1 1 1 
#     Output                    Output
#        2                        10

a=input().split()
new_list=[]
i=0
cnt=0
while i<len(a)-1:
	d=a[i]
	c=a[i+1]
	if d==c:
		cnt+=1
		a.pop(d)
	i+=1
print(cnt)