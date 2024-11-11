# nested loop = a loop within another loop (outer, inner)
    #outer loop:
        #inner loop:

# for x in range(1,10):
#     print(x, end='') #the (, end='' makes them all print on one line)

# for x in range(3): #outer loop
#     for y in range(1,10): #iner
#         print(y, end=' ')
#     print()

rows = int(input('enter the number of rows: '))
colums = int(input('enter the number of colums: '))
symbol = input('Enter a symbol to use: ')
for x in range(rows): #outer loop
    for y in range(colums): #iner
        print(symbol, end=' ')
    print()