from datetime import datetime
startTime = datetime.now()
import numpy as np
z=np.load('test.pickle')
a=np.array(z).reshape((3,3,3))
print("The newly Generated array is:")
print(a)
print("_______________________________")
print("Applying cubical add at edge length 2 ")
d=2 #depth of application
h=2 #height of application
w=2 #width of application
add=2 #number to be added
a[:d,:h,:w]=a[:d,:h,:w]+add
print(a)
print(datetime.now() - startTime) 
