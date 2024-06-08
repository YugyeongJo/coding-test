a,b,c = map(int, input().split())
dice = [a,b,c]

if dice[0]==dice[1]==dice[2] : 
    result = 10000+(dice[0]*1000)
    print(result)
elif dice[0]==dice[1] or dice[0]==dice[2]:
    result = 1000+(dice[0]*100)
    print(result)
elif dice[1]==dice[2]:
    result = 1000+(dice[1]*100)
    print(result)
else :
    result = max(dice)*100
    print(result)