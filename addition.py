def input1():
    print("Enter first number")
    a=input()
    print("Enter second number")
    b=input()
    x=int(a)
    y=int(b)

    return(x,y)

def compute(x,y):
    result=x+y
    return result

def output(res):
    print("Sum =",res)
    print(res)

def main():
    mylist=[]
    mylist=input1()
   
    r=compute(mylist[0],mylist[1])
   
    output(r)

main()

    
    
    
