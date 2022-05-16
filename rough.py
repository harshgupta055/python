# m, n = map(int, input().split())
# products = []
# for _ in range(m):
#     productsay2 = list(map(int, input().split()))
#     products.append(productsay2)

# largest = []
# for i in range(m):
#     for j in range(n):
#         if products[i][j] == 1:
#             k = 1
#             while i+k < m and j+k < n:
#                 if products[i][j+k] == 1 and products[i+k][j] == 1 and products[i+k][j+k] == 1:
#                     k += 1
#                 else:
#                     largest.append(k)
#                     break
#             largest.append(k)
#         else:
#             continue
# print(max(largest)**2)
                

products = list(map(int, input().split()))
price = list(map(int, input().split()))
k = int(input())

length = len(products)
for i in range(length):
    for j in range(0, length-i-1):
        if products[j] > products[j+1]:
            temp = products[j]
            temp2 = price[j]
            products[j] = products[j+1]
            price[j] = price[j+1]
            products[j+1] = temp
            price[j+1] = temp2
pay = 0
prod = 0
m = 0
while prod < k and m < length:
    prod += products[m]
    pay += price[m]
    m += 1
    if prod + products[m+1] > k:
        break
print(pay)
            
