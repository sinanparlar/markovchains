 

import random
import numpy as np
import time
  
def transition_matrix_generator(size):

    matrix = np.random.rand(size,size)
    matrix=matrix/matrix.sum(axis=1)[:,None]
    return matrix
    

#GENERATING RANDOM MATRICES
m5=transition_matrix_generator(5)
m25=transition_matrix_generator(25)
m50=transition_matrix_generator(50)


m5abs=m5.copy()
m5abs[3]=[0 for i in range(5)]
m5abs[3,3]=1

m25abs=m25.copy()
m25abs[3]=[0 for i in range(25)]
m25abs[3,3]=1

m50abs=m50.copy()
m50abs[3]=[0 for i in range(50)]
m50abs[3,3]=1



# MONTE CARLO SIMULATION
def method1(array,M=200000):
    x0=random.randint(0,np.shape(array)[0]-1)
    xc=x0
    values = dict([(str(i),0) for i in range(np.shape(array)[0])])
    
    
    for m in range(M):
        i=True
        a=0
        r= random.random()
        
        while i:
            
            z1=0
            z2=0
            for j in range(a+1):
                
                z2+=array[xc,j]
            for k in range(a):
                z1+=array[xc,k]
            if z1<=r<=z2:
                xc=a
                values[str(xc)]+=1/M
                i=False

            else:
                a+=1
    # for (k,v) in values.items():
    #     print(k,":",v)



# MATRIX MULTIPLICATION


def method2(array):
    
    eps=0.0005    
    i=True
    t=1
    while i:
        pi=array.sum(axis=0)/np.shape(array)[0]        #average of the rows
        rrow=array[random.randint(0,np.shape(array)[0]-1)] #random row
        a= np.absolute((pi-rrow)) < np.full((1, np.shape(array)[0]), eps) #returns an array with boolean values
       
        if a.all(): 
            # print(array[0])
            # print('t=',t)
            i=False
        else:
            array=np.matmul(array,array)
            t=t+1




def average_time(matrix_size,number_of_trials):   
    avgt1=0
    avgt2=0
    for i in range(number_of_trials):
        matrix=transition_matrix_generator(matrix_size)
        
        matrix[3]=[0 for i in range(matrix_size)] #for absorbing matrices
        matrix[3,3]=1                    #making the third state absorbing
        

        t1 = time.time()
        method1(matrix)
        t2=time.time()
        method2(matrix)
        t3=time.time()
        avgt1+=t2-t1
        avgt2+=t3-t2
    print('Monte Carlo Simulation took average of',avgt1/number_of_trials,'seconds in',  number_of_trials ,'trials when worked with', matrix_size,'x',matrix_size,'matrices')
    print('Matrix Multiplication Method took average of',avgt2/number_of_trials,'seconds in' , number_of_trials ,'trials when worked with', matrix_size,'x',matrix_size,'matrices')

average_time(50,10)



