N=int(input("Please enter the number of overs to be played : "))

print()

B=N*6 #No.of balls

S=0

W=0

Bp=1

SpB=list(input("Please enter the score per ball separarted by space, for out its is number + o, for wide it will be number + wd, for no ball it is number + nb, for leg bye it is number + lb and for bye it is number + b : ").strip().split())

print()

i=0

while(Bp<=B):
    if W<10:
        if  SpB[i]=="0" :
            S=S+0
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="1" :
            S=S+1
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="2" :
            S=S+2
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="3" :
            S=S+3
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="4" :
            S=S+4
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="5" :
            S=S+6
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="6" :
            S=S+6
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="0wd" :
            S=S+0+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="1wd" :
            S=S+1+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="2wd" :
            S=S+2+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="3wd" :
            S=S+3+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="4wd" :
            S=S+4+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="0nb" :
            S=S+0+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="1nb" :
            S=S+1+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="2nb" :
            S=S+2+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="3nb" :
            S=S+3+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="4nb" :
            S=S+4+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="5nb" :
            S=S+5+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="6nb" :
            S=S+6+1
            Bp=Bp+0
            i=i+1
        elif  SpB[i]=="1lb" :
            S=S+1
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="2lb" :
            S=S+2
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="3lb" :
            S=S+3
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="4lb" :
            S=S+4
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="1b" :
            S=S+1
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="2b" :
            S=S+2
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="3b" :
            S=S+3
            Bp=Bp+1
            i=i+1
        elif  SpB[i]=="4b" :
            S=S+4
            Bp=Bp+1
            i=i+1
        elif SpB[i]=="0o":
            S=S+0
            Bp=Bp+1
            W=W+1
            i=i+1
        elif  SpB[i]=="1o" :
            S=S+1
            Bp=Bp+1
            W=W+1
            i=i+1
        elif  SpB[i]=="2o" :
            S=S+2
            Bp=Bp+1
            W=W+1
            i=i+1
        elif  SpB[i]=="3o" :
            S=S+3
            Bp=Bp+1
            W=W+1
            i=i+1
    else:
        break
print("The team played "+str((Bp-1)//6)+"."+str((Bp-1)%6)+" over and has achieved a score of : "+str(S)+"/"+str(W))
        
