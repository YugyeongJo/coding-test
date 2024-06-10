S = input()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# alphabet = list(range(97,123))  # 아스키코드 활용

input_str = []
for value in S:
    if value not in input_str:
        input_str.append(value)

list_result = []
for x in alphabet:
    if x in S:      
        result = S.index(x)
        list_result.append(result)
    else : 
        list_result.append(-1)
        
print(*list_result)