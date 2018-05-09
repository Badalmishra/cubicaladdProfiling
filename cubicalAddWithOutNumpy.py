from datetime import datetime
startTime = datetime.now()
import pickle
n=3
dis=pickle.load(open('test.pickle','rb'))
t=0
distance = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
for p in range(n):
    for q in range(n):
        for r in range(n):
            distance[p][q][r]=dis[t]
            t=t+1
def show():
    for p in range(n):
        print("")
        for q in range(n):
            print("")
            for r in range(n):
                print(str(distance[p][q][r])+" ",end='')
    print()
print("The newly Generated array is:")
show()
def cubeadd():
    a=2 #number to be added
    b=2 #depth of application
    c=2 #width of application
    d=2 #height of application
    for p in range(b):
        for q in range(c):
            for r in range(d):
                distance[p][r][q]=distance[p][r][q]+a
    print("new array")
print("Applying cubical add at edge length 2 ")
cubeadd()
show()
print(datetime.now() - startTime) 
