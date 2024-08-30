n=int(input())
count = 1
sum_of_squares = 0
while count <= n:
    sum_of_squares = sum_of_squares + (count ** 2)
    count = count + 1
print(sum_of_squares)