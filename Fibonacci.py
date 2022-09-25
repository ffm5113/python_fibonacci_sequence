class Fibonacci:
    print('Fibonacci showed us that humans have a remarkable ability to identify patterns:')
    n = 20    # Number of iterations
    index = 0 # Object to keep track of iteration index
    x = 0     # Value printed on first iteration/calculated value based on iteration index
        
    def integers(self):
        # While the iteration index is less than 20
        while self.index < self.n:                                                    
            # Golden Ratio equation based on current index    
            self.x = (1.618034**(self.index) - (1-1.618034)**(self.index))/(math.sqrt(5)) 
            # Round the value so that it is a whole number
            self.x = round(self.x)                           
            # Print each iteration space-delimited                             
            print(self.x, end=' ')
            # Raise the index while it is less than 20                                                        
            self.index += 1                                                               
          
# Define main method  
def main():                        
    # Declare object fibonacci of class Fibonacci
    fibonacci = Fibonacci()        
    # Call integers methods/function
    fibonacci.integers()           
    
if __name__ == '__main__': main()

# OUTPUT
# Fibonacci showed us that humans have a remarkable ability to identify patterns:
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
