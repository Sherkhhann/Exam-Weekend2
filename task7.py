# 7:
#     Given a list of numbers. Count how many pairs of elements are in it that are equal to each other. It is believed that any two elements equal to each other form one pair that must be counted.

#     Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

#     Input data                Input data
#        1 2 3 2 3                1 1 1 1 1 
#     Output                    Output
#        2                        10

a = input().split()
cnt = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            cnt += 1
print(cnt)