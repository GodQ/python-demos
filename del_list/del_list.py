l = [0,1,2,3,4,5,6,7]

for i in range(len(l)-1, -1, -1):
    print(i)
    if l[i]%2==0:
        del l[i]
        print("del %d"%i)

print(l)
