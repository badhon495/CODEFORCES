a,b = map(int, input().split())
u_input = input()
for _ in range(b):
    temp_input = u_input
    for i in range(0,a+1,2):
        if temp_input[i]=='B':
            u_input = temp_input[i+1]+temp_input[i]
        else:
            u_input += temp_input[i]

print(u_input)
