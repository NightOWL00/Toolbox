# IDEA : A simple script to create a index file for courses and managing notes.

x=' '
c=0
a=open('Index.txt','w')
a.close()
print("Enter 's' for section and 'tx' for topic, where x is the number of sections or topics")
while x.lower()!='exit':
    x = input(">>>  ").lower()
    if x[0]=='s':
        section=input("Enter section :  ")
        with open('Index.txt','a') as f:
            f.write('-~-~- '+ section +' -~-~-\n')

    elif x[0]=='t':
        with open('Index.txt','a') as f:
            for i in range(int(x[1])):
                topic=input("Enter Topic :  ")
                c+=1
                f.write('\t'+str(c)+'. '+topic+'\n')
    elif x=='exit':
        print("bye-bye")
    else:
        print("Wrong input.\nIf you wanna exit enter 'exit'.\n")