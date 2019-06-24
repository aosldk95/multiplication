# 2520은 1부터 10까지의 숫자로 모두 나눠지는 최소의 수입니다.
# 1부터 20까지의 숫자로 모두 나눠지는 최소의 수를 구하세요.
number = 20
numberlist = []
j = 2
for i in range (2, number +1) :
    line = []
    while j < i + 1 :
        if (i % j) == 0 :
            line.append(j)
            i /= j
            j = 2
        else :
            j += 1
    numberlist.append(line)
for i in numberlist :
    for j in numberlist[i] :

#temp1 = ['One', 'Two', 'Three', 'Four']
#temp2 = ['One', 'Two']
#temp3 = []
#for i in temp1:
#    if i not in temp2:
#        temp3.append(i)



print(max(numberlist))

            
            
    
