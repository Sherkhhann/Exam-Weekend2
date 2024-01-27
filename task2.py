# 2:
#     The sequence consists of natural numbers and ends with the number 0. Determine the value of the largest element of the sequence. Numbers following zero do not need to be read.

#     Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности. Числа, следующие за нулем, считывать не нужно.
#     Input data
#     1
#     7
#     9
#     0

#     Output
#     9 
maxx=-99999
while True:
	a=int(input())
	if a==0:
		break
	else:
		if a>maxx:
			maxx=a
print(maxx)
