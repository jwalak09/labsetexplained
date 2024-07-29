#hill climb
import random
def fitness(sol):  #to find the sum of solution of the alg
    return sum(sol)
def solution(num): #function to find the best soln
    current_soln = [random.randint(0,1) for _ in range(0,num)]
    current_fit = fitness(current_soln)
    while True:
        index=random.randint(0,num-1) #choosing a random index to start the climbing
        neighbor=current_soln[:] #copy the curentsoln to neighbor
        neighbor[index]=1-neighbor[index] #flips the binary value to go to the next neighbor
        neighbor_fit=fitness(neighbor)#to evaluate the fitness of neighbor we copy neighbor
        # into this
        if neighbor_fit>=current_fit:#If the neighbor solution is better (i.e., has higher fitness),
            # update the current solution and fitness.
            current_fit=neighbor_fit
            current_soln=neighbor
        else:
            break
    return current_soln,current_fit
best_soln,best_fit= solution(3) #specify the length of solution vector can be random
print('best soln=',best_soln)
print('best fitnes=',best_fit)
