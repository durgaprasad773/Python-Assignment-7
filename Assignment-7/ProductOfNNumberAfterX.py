x=int(input())
n=int(input())
product = 1
count = 1
while count <=n:
    product = product * (x+count)
    count = count + 1
print(product)