import random
import operator
import matplotlib.pyplot

# first thing is to define the agents that our model will use, these agents can move and eat the environment that they are in 


class Agent:
    def __init__ (self,agents,environment,x = None,y = None):
        self.agents = agents 
# this next code give the agents a random starting point on the grid and then keeps them from becomin another random point each time, this is done for both x and y coordinates        
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
#   this next section makes the agent interact with the environment when it moves to a new space   
#    def init (self,environment):
        self.environment = environment
        self.store = 0 # We'll come to this in a second.
        
        
        
        
    
# The next bit of code allows our agents to move it generates a random number between 0 and 1 and if it is below 0.5 then the agent will move one space positively and if it is above it will move onespace negatively    
    def move (self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
    
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
#        the sheep now eat the environment and is shown on the model by a colour change
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
#                print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5




        
# the next piece of code sets up a predator that will eventually interact with the agents 
class Predator:
    def __init__ (self,predator,x = None,y = None):
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
#  again we have the predators placed in a random point on the environment and then it moves from that spot           
    
# for the predators i wanted them to move faster than the agents as they dont interact with the environment like the agents do so i have coded them to move spaces with each iteration of the model         
    def move (self):
        if random.random() < 0.5:
            self._x = (self._x + 2) % 100
        else:
            self._x = (self._x - 2) % 100
        if random.random() < 0.5:
            self._y = (self._y + 2) % 100
        else:
            self._y = (self._y - 2) % 100
    
#    def kill (self,killrange):
#        for predator in self.predator:
#            dist = self.distance_between(predator)
#            if dist <= killrange:
                
#     def distance_between(self.predator):   
#          return (((self._x - predator._x)**2) + ((self._y - predator._y)**2))**0.5  
            
#struggled to get the predators to delete from the list of agents based on location        
        

 



