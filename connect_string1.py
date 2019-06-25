def input_info():
    print("Enter  Server name:")
    server=input()
    print("Enter database name:")
    dbname=input()
    print("Enter user name:")
    user=input()
    print("Enter the password:")
    pasw=input()

    return("server=%s;dbname=%s;usr=%s;pass=%s"%(server,dbname,user,pasw))
    
def cstolot(cs):
    l=[]
    for i in cs.split(";"):
        l.append(tuple(i.split("=")))
    return l     

    

def main():
  
    cs=input_info()
    print(cs)
    
    print(cstolot(cs))
    

main()

