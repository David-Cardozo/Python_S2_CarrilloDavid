############################################

if __name__ == '__main__':
    print("Hello, World!")

############################################

if __name__ == '__main__':
    n = int(input().strip())

if (n % 2 != 0):
    print("Weird")
elif (n % 2 == 0 and n > 2 and n < 5):
    print("Not Weird")
elif (n % 2 == 0 and n > 6 and n < 20):
    print("Weird")
elif (n % 2 == 0 and n > 20):
    print("Not Weird")
else:
    print("Weird")

############################################

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    sum = a  + b
    diffe = a - b
    product = a * b
    
    if (1 <= a <= 10**10 and 1 <= b <= 10**10):
        print(sum)
        print(diffe)
        print(product)

############################################

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    div1 = a // b
    div2 = float(a / b)
    
    print(div1)
    print(div2)

############################################

if __name__ == '__main__':
    n = int(input())
    
for i in range(n):
    print(i ** 2)

############################################

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
list = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i + j + k != n):
                list.append([i , j , k])
print(list)

############################################



############################################
