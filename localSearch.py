# coding: utf-8

# Jeremy Aguillon
# Project 2
# CMSC 471
# 20 March 2016
# This is my code to implement hill climbing, 
# hill climbing with random restarts and 
# simulated annealing local search algorithms



import matplotlib.pyplot as plt
import numpy as np

# Search input variables
X_MIN = -2.5
X_MAX = 2.5
Y_MIN = -2.5
Y_MAX = 2.5
STEP = .05
RESTARTS = 100
MAX_TEMP = 1000

# Main function
def main():
    '''
    #old test cases
    print("Test function: sinc(x) + sinc(y)")
    localMin, xVal, yVal = hill_climb(sincFn, STEP, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Basic Hillclimbing \nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    localMin, xVal, yVal = hill_climb_random_restart(sincFn, STEP, RESTARTS, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Hillclimbing with restarts\nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    simulated_annealing(sincFn, STEP, MAX_TEMP, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Simulated Annealing\nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
  

    print("Test function: tan(x) * tan(y)")
    localMin, xVal, yVal = hill_climb(tantan, STEP, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Basic Hillclimbing \nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    localMin, xVal, yVal = hill_climb_random_restart(tantan, STEP, RESTARTS, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Hillclimbing with restarts\nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    localMin, xVal, yVal = simulated_annealing(tantan, STEP, MAX_TEMP, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Simulated Annealing\nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    

    print("Test function: x * y")
    localMin, xVal, yVal = hill_climb(xTimesY, STEP, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Basic Hillclimbing \nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    localMin, xVal, yVal = hill_climb_random_restart(xTimesY, STEP, RESTARTS, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Hillclimbing with restarts\nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    localMin, xVal, yVal = simulated_annealing(xTimesY, STEP, MAX_TEMP, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Simulated Annealing\nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    '''
    # Testing the given function for part 2
    print("Test function: long one")
    localMin, xVal, yVal = hill_climb(realFn, STEP, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Basic Hillclimbing \nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    localMin, xVal, yVal = hill_climb_random_restart(realFn, STEP, RESTARTS, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Hillclimbing with restarts\nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    localMin, xVal, yVal = simulated_annealing(realFn, STEP, MAX_TEMP, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Simulated Annealing\nlocalMIN:",localMin, "x:",xVal,"y:",yVal)


# hill_climb() performs a single hill climbing search on a given function with given parameters
# Input: function_to_optimize - a pointer to a function that this code searches
#        step_size - the amount moved each time a move is made
#        xmin/ymin - the minimum values that x or y can contain
#        xmax/ymax - the maximum values that x or y can contain
# Output: curMin - the local minimum found with the hill climbing search
#         curX - the x value of the function at the local minimum
#         curY - the y value of the function at the local minimum
def hill_climb(function_to_optimize, step_size, xmin, xmax, ymin, ymax):
    # selects random starting point
    curX = np.random.uniform( xmin, xmax )
    curY = np.random.uniform( ymin, ymax )
    curMin = function_to_optimize(curX, curY)
    # while loop flag
    searching = True

    # searches the function until a local minimum is found
    while(searching):
        #print("curMIN:",curMin, "x:",curX,"y:",curY)

        # stores each possible step in an array to check if they are in bounds and less than curMin
        tempMin = [function_to_optimize(curX+step_size, curY), function_to_optimize(curX-step_size, curY), function_to_optimize(curX, curY+step_size), function_to_optimize(curX, curY-step_size)]
        
        # finds a lower minimum and updates it or ends the loop
        if( curX+step_size <= xmax and tempMin[0] < curMin ):
            curX = curX + step_size
            curMin = function_to_optimize(curX, curY)
        elif( curX-step_size >= xmin and tempMin[1] < curMin ):
            curX = curX - step_size
            curMin = function_to_optimize(curX, curY)
        elif( curY+step_size <= ymax and tempMin[2] < curMin ):
            curY = curY + step_size
            curMin = function_to_optimize(curX, curY)
        elif( curY-step_size >= ymin and tempMin[3] < curMin ):
            curY = curY - step_size
            curMin = function_to_optimize(curX, curY)
        else:
            #print("Local min or plateau or something\ncurMin",curMin,"\ntempmins", tempMin)
            searching = False

    #print("end loop - min:",curMin)
    #print("localMin:",curMin, "x:",curX,"y:",curY)
    return curMin, curX, curY


# hill_climb_random_restart() performs multiple hill climbing searches on a given function with given parameters
# Input: function_to_optimize - a pointer to a function that this code searches
#        step_size - the amount moved each time a move is made
#        num_restarts - the number of times hill climbing will be applied to the function
#        xmin/ymin - the minimum values that x or y can contain
#        xmax/ymax - the maximum values that x or y can contain
# Output: curMin - the local minimum found with the hill climbing search
#         curX - the x value of the function at the local minimum
#         curY - the y value of the function at the local minimum
def hill_climb_random_restart(function_to_optimize, step_size, num_restarts, xmin, xmax, ymin, ymax):
    # initial values
    curMin, curX, curY = hill_climb(function_to_optimize, step_size, xmin, xmax, ymin, ymax)
    
    # performs hill climbing the number of times given
    for i in range(num_restarts - 1):
        tempMin, xVal, yVal = hill_climb(function_to_optimize, step_size, xmin, xmax, ymin, ymax)
        
        #print("tempMin:",tempMin, "curMin: ",curMin,"x:",xVal,"y:",yVal)
        
        # updates the current min if it is lower
        if tempMin < curMin:
            #print("updating curmin")
            curMin = tempMin
            curX = xVal
            curY = yVal
            
    return curMin, curX, curY


# simulated_annealing() does the simulated annealing algorithm on the function
#                       which starts out making random moves good or bad and 
#                       makes only good moves as the temperature lowers
# Input: function_to_optimize - a pointer to a function that this code searches
#        step_size - the amount moved each time a move is made
#        max_temp - the starting temperature of the function
#        xmin/ymin - the minimum values that x or y can contain
#        xmax/ymax - the maximum values that x or y can contain
# Output: curMin - the local minimum found with the hill climbing search
#         curX - the x value of the function at the local minimum
#         curY - the y value of the function at the local minimum
def simulated_annealing(function_to_optimize, step_size, max_temp, xmin, xmax, ymin, ymax):
    # amount the temperature will cool each iteration
    COOLING = .90
    
    # probablity() performs the e^(new-old)/t calculation
    def probability(prev, cur, temp):
        return np.exp( (prev - cur)/temp )
    
    # gets random starting point
    curX = np.random.uniform( xmin, xmax )
    curY = np.random.uniform( ymin, ymax )
    xVal = curX
    yVal = curY
    curMin = function_to_optimize(curX, curY)
    
    #print("Starting SA\nlocalMin:",curMin, "x:",curX,"y:",curY)

    # loops until the temperature has fully cooled
    while( max_temp >= .0001):
        # gets all possible moves and stores them
        tempMin = [function_to_optimize(curX+step_size, curY), function_to_optimize(curX-step_size, curY), function_to_optimize(curX, curY+step_size), function_to_optimize(curX, curY-step_size)]
        legalChange = [curX+step_size <= xmax, curX-step_size >= xmin, curY+step_size <= ymax, curY-step_size >= ymin]
        tempChange = [curX+step_size, curX-step_size, curY+step_size, curY-step_size]
        # picks a random direction - 0 = x + step | 1 = x - step | 2 = y + step | 3 = y - step
        direction = np.random.randint(4)
        
        # updates if the new move is lower than the local min
        if( legalChange[direction] and tempMin[direction] < curMin ):
            if direction in [0,1]:
                curX = tempChange[direction]
            elif direction in [2,3]:
                curY = tempChange[direction]
            #print("updating min - tempMin:",tempMin[direction],"curMin", curMin,"temp",max_temp)

            curMin = function_to_optimize(curX, curY)

            # stores coordinates of local min to return
            xVal = curX
            yVal = curY
            
        # not a new local min
        else:
            # compares the probability to a random number between 0 and 1 to see if it will make a bad move
            prob = probability(curMin, tempMin[direction], max_temp)
            randNum = np.random.random()
            if prob > randNum:
                if direction in [0,1]:
                    curX = tempChange[direction]
                elif direction in [2,3]:
                    curY = tempChange[direction]       
                #print("making bad move - tempMin:",tempMin[direction],"curMin", curMin,"probability", prob, "random", randNum,"temp",max_temp)

        # cools the temperature
        max_temp *= COOLING
    
    return curMin, xVal, yVal
        

## TEST FUNCTIONS ##
# sunc functions with multiple local minimums
def sincFn(x,y):
    if type(x) in [int, float] and type(y) in [int, float]:
        return float( np.sinc(x) + np.sinc(y) )
    else:
        return False

# tan of both x and y with empty areas in the search space
def tantan(x,y):
    if type(x) in [int, float] and type(y) in [int, float]:
        return float( np.tan(x) * np.tan(y) )
    else:
        return False


# a flat surface to search
def xTimesY(x,y):
    if type(x) in [int, float] and type(y) in [int, float]:
        return float( x * y )
    else:
        return False


# given function in part 2 to search
def realFn(x,y):
    if type(x) in [int, float] and type(y) in [int, float]:
        r = np.sqrt(x**2 + y**2)
        return ( np.sin(x**2 + 3*(y**2))/(.1 + r**2) ) + (x**2 + 5*(y**2)) * ( np.exp(1-r**2)/2 )
    else:
        return False


# call to main
main()

