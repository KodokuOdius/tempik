
# Pascal`s Triangle
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1


n = int(input('Введите высоту треугольника: '))

triangle = []
for i in range(1, n+1):
    temp = [1]
    if i == 2:
        temp.append(1)
    elif i > 2:
        for j in range(1, len(triangle[i-2])):
            temp.append(triangle[i-2][j-1] + triangle[i-2][j])
        temp.append(1)
    triangle.append(temp)


for el in triangle:
    #print('\t' * (n-len(el)), end='')
    print(*el)


