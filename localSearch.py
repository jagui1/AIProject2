
# coding: utf-8

# In[93]:

import matplotlib.pyplot as plt
import numpy as np
import random

X_MIN = -2.5
X_MAX = 2.5
Y_MIN = -2.5
Y_MAX = 2.5
STEP = .5
RESTARTS = 5

def main():
    print("Test function: sinc(x) + sinc(y)")
    localMin, xVal, yVal = hill_climb(funcToOpt, STEP, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Basic Hillclimbing \nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    localMin, xVal, yVal = hill_climb_random_restart(funcToOpt, STEP, RESTARTS, X_MIN, X_MAX, Y_MIN, Y_MAX)
    print("Hillclimbing with restarts\nlocalMIN:",localMin, "x:",xVal,"y:",yVal)
    simulated_annealing(funcToOpt, 1, 98, X_MIN, X_MAX, Y_MIN, Y_MAX)


# In[94]:

def hill_climb(function_to_optimize, step_size, xmin, xmax, ymin, ymax):
    curX = random.randint( np.floor(xmin), np.ceil(xmax) )
    curY = random.randint( np.floor(ymin), np.ceil(ymax) )
    curMin = function_to_optimize(curX, curY)
    searching = True

    while(searching):
        #print("curMIN:",curMin, "x:",curX,"y:",curY)
        
        tempMin = [function_to_optimize(curX+step_size, curY), function_to_optimize(curX-step_size, curY), function_to_optimize(curX, curY+step_size), function_to_optimize(curX, curY-step_size)]
        
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


# In[95]:

def hill_climb_random_restart(function_to_optimize, step_size, num_restarts, xmin, xmax, ymin, ymax):
    curMin, curX, curY = hill_climb(function_to_optimize, step_size, xmin, xmax, ymin, ymax)
    
    for i in range(num_restarts - 1):
        tempMin, xVal, yVal = hill_climb(function_to_optimize, step_size, xmin, xmax, ymin, ymax)
        
        #print("tempMin:",tempMin, "curMin: ",curMin,"x:",xVal,"y:",yVal)
        
        if tempMin < curMin:
            #print("updating curmin")
            curMin = tempMin
            curX = xVal
            curY = yVal
            
    return curMin, curX, curY


# In[96]:

def simulated_annealing(function_to_optimize, step_size, max_temp, xmin, xmax, ymin, ymax):
    print("Simulated annealing")


# In[97]:

def funcToOpt(x,y):
    if type(x) in [int, float] and type(y) in [int, float]:
        return float( np.sinc(x) + np.sinc(y) )
    else:
        return False


# In[98]:

main()


# In[ ]:



