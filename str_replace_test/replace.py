import time

s1="11111111111111111111111111111111111111111111111111111111111111aaaaaa111111111111111111111111"
s2="11111111111111111111111111111111111111111111111111111111111111bbbbbb111111111111111111111111"
count = 10000000

start = time.time()

for i in range(count):
    if i%2 == 0:
        s = s1
    else:
        s = s2
    s.replace("aaaaaa", "")

end = time.time()

print("replace: {}".format(end-start))



start = time.time()

for i in range(count):
    if i%2 == 0:
        s = s1
    else:
        s = s2
    if s.find("aaaaaa") > -1:
        s.replace("aaaaaa", "")

end = time.time()

print("find and replace: {}".format(end-start))
