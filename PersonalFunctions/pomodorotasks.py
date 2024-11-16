#import random for random operations
import random

#create list of task items and number of iterations
#to use this for yourself, just copy and change out the tasks and add the cycle counts you prefer
tasks = ["3D Print", "Wood Carving", "Crochet", "Code", "Robotics", "Video Games"]

cycles = [1, 2, 3, 4]

#prints a random item from each list to set Number of pomodoro sessions and activity
print(random.choice(cycles));
print(random.choice(tasks));