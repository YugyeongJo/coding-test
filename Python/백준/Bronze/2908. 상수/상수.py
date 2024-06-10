a, b = input().split()
a= list(a)
b= list(b)
revers_a = ''.join(reversed(a))
revers_b = ''.join(reversed(b))

if revers_a > revers_b:
    result = revers_a
elif revers_a < revers_b:
    result = revers_b
else: 
    result = revers_a
    
print(result)