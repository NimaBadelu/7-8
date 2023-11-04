n = int(input(" Enter a row: "))
m = int(input(" Enter a column: "))
a = 1 
for i in range(1, n+1):
    for j in range(1, m+1):
        if a == 1:
            print(end="*")
        else:
            print(end="#")

        a = -a
    if m %2 == 0:
        a*=-1
    print()