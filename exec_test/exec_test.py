
print('\n\n\n\ntest1:')
inserted_code = \
'''print(a)
print(b)
c = a + b
'''


a = 1
b = 2
print(locals())
exec(inserted_code)
print(locals())
print(c)


