def check(a):
    for i in range(3):
        st=a[i][0]
        c1=0
        for j in range(3):
            if(a[i][j]==st):
                    c1+=1
        if(c1==3):
            if(st==ch1):
                return 1
            else:
                return 0
        st=a[0][i]
        c1=0
        for j in range(3):
            if(a[j][i]==st):
                 c1+=1
        if(c1==3):
            if(st==ch1):
                return 1
            elif(st==ch2):
                return 0
       
    c1=0;c2=0
    for i in range(3):
        for j in range(3):
            st=a[0][0]
            if(i==j):
                if(a[i][j]==st):
                    c1+=1
            st=a[0][2]
            if(i+j==2):
                if(a[i][j]==st):
                    c2+=1
    if(c1==3 or c2==3):
        if(st==ch1):
            return 1
        elif(st==ch2):
            return 0
    return -1
a=[]
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(" ")
print("********************************TIC TAC TOE************************************\n")
ch1=input("choose any character(player 1):")
ch2=input("choose any character(player 2):")
for i in range(9):
    if(i%2==0):
        m=int(input("ROW position (player one),choices[1,2,3]"))
        n=int(input("COL position (player one),choices[1,2,3]"))
        while( m<1 or m>3 or n<1 or n>3 or a[m-1][n-1]==ch1 or a[m-1][n-1]==ch2):
            print("\n\t~~~~~~~~~~~~~~~INVALID INPUT~~~~~~~~~~~~~~\n")
            m=int(input("ROW position (player one),choices[1,2,3]"))
            n=int(input("COL position (player one),choices[1,2,3]"))
        a[m-1][n-1]=ch1
            
    else:
        m=int(input("ROW position (player two),choices[1,2,3]"))
        n=int(input("COL position (player two),choices[1,2,3]"))
        while( m<1 or m>3 or n<1 or n>3 or a[m-1][n-1]==ch1 or a[m-1][n-1]==ch2):
            print("\n\t~~~~~~~~~~~~~~~~INVALID INPUT~~~~~~~~~~~~~\n")
            m=int(input("ROW position (player two),choices[1,2,3]"))
            n=int(input("COL position (player two),choices[1,2,3]"))
        a[m-1][n-1]=ch2
    for j in range(3):
        for k in range(3):
            print('|',a[j][k],end=' ')
        print('|')
        print('--------------')
    if(i>3):
        if(check(a)==1):
            print("*********************PLAYER ONE WINS**********************")
            break
        elif(check(a)==0):
            print("*********************PLAYER TWO WINS**********************")
            break
if(check(a)==-1):
    print("oops!!!! this is tie")
        
                    
