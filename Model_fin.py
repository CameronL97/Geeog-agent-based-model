import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import requests
import bs4
import csv
import tkinter


environment =[]

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
p_ys = soup.find_all(attrs={"class" : "y"})
p_xs = soup.find_all(attrs={"class" : "x"})
with open ('in.csv') as f:
    readCSV = csv.reader(f,delimiter = ',')
    for row in readCSV:
        rowlist = []
        for value in row:
            #print(float(value))
            rowlist.append(int(value))
        environment.append(rowlist)
#opens the csv and appends the environmental data into the array 
#matplotlib.pyplot.ylim(0, 100)
#matplotlib.pyplot.xlim(0, 100)
#matplotlib.pyplot.imshow(environment)
 
#create the number of agents used in this case we'll call them sheep
num_of_agents = 10
#create the number of predators used 
num_of_predator = 5
#create the number of iterations or for how many times the prgram will run till the stop condtion is met
num_of_iterations = 1000
#create the neighbourhood
neighbourhood = 20
#create an agents list to append data to later 
agents = []
#create a predator list to append data to later
predator = []
#create a killrange for the predators
#killrange = 5



#create the plot are that our agents and predators will be located in 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 101, 0, 101])

#stops the plot from scaling itself
ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(agents,environment,x, y))
#appends the x,y coordinates from the agentframework model to the agent list  
carry_on = True	


	
# Make the predators.
for i in range(num_of_predator):
    y = int(p_ys[i].text)
    x = int(p_xs[i].text)
#    appends the predator x,y coordinates from agentframework model to the predator list
    predator.append(agentframework.Predator(predator,x, y))

carry_on = True	

def update(frame_number):
    
    fig.clear()   
    global carry_on
    
# one update for the model would be to essentially fence in the agents as they can drift from each side of the model as they move essentially teleporting in a real life situation which would not be possible, however if we view the world in the model as a donut then the model conforms to real world conditions 
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
#    if random.random() < 0.1:
#        carry_on = True
#        print("stopping condition")

        #print(agents[i][0],agents[i][1])


    for i in range(num_of_predator):
        predator[i].move()
#        predator[i].share_with_neighbours(neighbourhood)
#        
#    if random.random() < 0.1:
#        carry_on = True
##        print("stopping condition")
# 
#

    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_predator):
        matplotlib.pyplot.scatter(predator[i]._x,predator[i]._y, color = 'red') #changed the predators to red to distinguish between the two agents shown
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y, color = 'black') # agents in this case "sheep" are black 
##matplotlib.pyplot.imshow(environment)		
#this runs the model for the number of iterations and then stops the model with the word "stopped" to show that it has finished fully and the model hasnt run into a problem and stopped early
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 1000) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
    if a > 1000:
        carry_on = False
#    print ("stopped")
#this code did not originally print stopped due to wrong indentation it now correctly tells you when the model has stopped 

#to make the stopping conditon for the model better you could make it stop after all of the environment has been eaten or the predators have killed the agents  

##animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

root = tkinter.Tk()
root.wm_title("Model")
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


tkinter.mainloop()