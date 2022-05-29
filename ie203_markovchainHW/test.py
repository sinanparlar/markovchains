 
import random
import numpy as np
  
def transition_matrix_generator(size):

    matrix = np.random.rand(size,size)
    matrix=matrix/matrix.sum(axis=1)[:,None]
    return matrix
    

# GENERATING RANDOM MATRICES
m5=transition_matrix_generator(5)
m25=transition_matrix_generator(25)
m50=transition_matrix_generator(50)

# MONTE CARLO SIMULATION
def method1(array):
    x0=random.randint(0,np.shape(array)[0]-1)
    xc=x0
    values = dict()
    
    
    
    for m in range(300):
        i=True
        a=0
        r= random.random()
        while i:
            
            z1=0
            z2=0
            for j in range(a+1):
                o=array[xc,j]
                z2+=array[xc,j]
            for k in range(a):
                z1+=array[xc,k]
            if z1<=r<=z2:
                xc=a
                if(str(xc) in values.keys()):
                    values[str(xc)]+=1/300
                else:
                    values[str(xc)]=1/300
                i=False

            else:
                a+=1
    print(values)
method1(m5)
