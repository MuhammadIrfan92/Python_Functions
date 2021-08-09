

def fibo(n):
    li=[]
    for i in range(n):
        if i<=1:
            li.append(i)
            l=li[i]
            print(l)

        else:
            l=li[i-1]+li[i-2]
            li.append(l)
            print(l)
    
            

if __name__ == '__main__':
    (fibo(8))
    


    
    
