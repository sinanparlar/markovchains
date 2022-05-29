## IE 203 - HOMEWORK 2 
# NECDET SINAN PARLAR

### Monte Carlo Simulation and Matrix Multiplication algorithms both succeed to compute the steady state probabilities of transition probability matrices. However, when we compare the compiling times, there is a significant difference between two methods.

- Matrix Multiplication Method took average of 0.0009071588516235352seconds in 10 trials when worked with 5x5 matrices.
- Matrix Multiplication Method took average of 0.00156097412109375 seconds in 10 trials when worked with 25x25 matrices.
- Matrix Multiplication Method took average of 0.002059173583984375 seconds in 10 trials when worked with 50 x 50 matrices.

#### Whereas;

+ Monte Carlo Simulation took average of 0.865449070930481 seconds in 10 trials when worked with 5x5 matrices.
+ Monte Carlo Simulation took average of 11.9608145236969 seconds in 10 trials when worked with 25x25 matrices.
+ Monte Carlo Simulation took average of 75.50835583209991 seconds in 10 trials when worked with 50x50 matrices.

### We can easily conclude that; 
- Matrix Multiplication Method is faster. 
- Both methods take more time when size of the matrix increases.

### In matrix multiplication method;
- If we decrease the value of epsilon, we get a more precise estimation of the steady state probability. Thus, in theory, if we make Epsilon=0 matrix multiplication method will return the exact value of the steady state probabilities.

- As the size of the transition probability matrix increases, number of iterations decreases.
	+ 5x5 matrices’ steady state probabilities are found in 4 iterations on average. 
    + 25x25 matrices’ steady state probabilities are found in 3 iterations on average.
    + 50x50 matrices’ steady state probabilities are found in 2 iterations on average.

Even though number of iterations decrease as the matrix size increases, compiling time increases. Because multiplying greater sizes of matrices takes longer time.



### In Monte Carlo simulation;
- If we increase the value of M(number of iterations) we get a more precise estimation of the steady state probability. Thus, in theory, if we iterate infinitely many times Monte Carlo simulation will return the exact value of the steady state probabilities.

### If one of the states in each matrix becomes absorbing;



- Matrix Multiplication Method took average of 0.0 seconds in 10 trials when worked with 5 x 5 matrices
- Matrix Multiplication Method took average of 0.001604008674621582 seconds in 10 trials when worked with 25 x 25 matrices
- Matrix Multiplication Method took average of 0.00017397403717041017 seconds in 10 trials when worked with 50 x 50 matrices

#### Whereas;

- Monte Carlo Simulation took average of 1.3961224555969238 seconds in 10 trials when worked with 5 x 5 matrices
- Monte Carlo Simulation took average of 1.6893239498138428 seconds in 10 trials when worked with 25 x 25 matrices
- Monte Carlo Simulation took average of 2.1334489583969116 seconds in 10 trials when worked with 50 x 50 matrices

It is obvious that compliling times drastically decreases in Monte Carlo Simulation and moderately decreases in Matrix Multiplication especially when work with 50x50 matrices.
