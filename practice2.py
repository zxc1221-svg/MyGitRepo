bro=list(map(int,input())) #哥哥出的第一個拳
sisN=int(input())#妹妹準備出幾回合的拳
sis=list(map(int,input().split()))#妹妹出的拳

bro.append(sis[0])


#如果妹妹連續兩次出一樣的拳 下一次就出這次可以打敗妹妹的拳
#否則哥哥出的拳是妹妹上一輪出的拳

for i in range(1,sisN-1):
    if sis[i]==sis[i-1]:
        if sis[i]==0:
            bro.append(5)
        elif sis[i]==2:
            bro.append(0)
        elif sis[i]==5:
            bro.append(2)
    else:
        bro.append(sis[i])
            
        
R=1
for i in range(sisN):
    if bro[i]==0:

        if sis[i]==0:
            R+=1
            
        elif sis[i]==2:
            for j in range(R):
                print(bro[j],end="7 ")
            print(": Won at round",R)
            break

        elif sis[i]==5:
            for j in range(R):
                print(bro[j],end=" ")
            print(": Lost at round",R)
            break

    elif bro[i]==2:

        if sis[i]==0:
            for j in range(R):
                print(bro[j],end=" ")
            print(": Lost at round",R)
            break

        elif sis[i]==2:
            R+=1

        elif sis[i]==5:
            for j in range(R):
                print(bro[j],end=" ")
            print(": Won at round",R)
            break

    elif bro[i]==5:

        if sis[i]==0:
            for j in range(R):
                print(bro[j],end=" ")
            print(": Won at round",R)
            break

        elif sis[i]==2:
            for j in range(R):
                print(bro[j],end=" ")
            print(": Lost at round",R)
            break

        elif sis[i]==5:
            R+=1

else:
    for j in range(sisN):
        print(bro[j],end=" ")
    print(": Drew at round",sisN)







