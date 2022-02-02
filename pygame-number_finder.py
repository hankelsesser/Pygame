import pygame as pg, sys
pg.init()

size = width, height =  800, 800
speed = [2, 2]
black = 0, 0, 0
screen = pg.display.set_mode(size)

import random
import math
class Agent:
    def __init__(self, fitness_condition):
      self.condition= fitness_condition
      self.score = 0
      self.color = 0, 0, 0


goal = random.randint(50,750)

def create(previous, round):
    agents=[]
    if previous != None:
        for i in range (10):
            agent_value = previous - random.randint(-50,50)
            agents.append(Agent(agent_value))
    else:
        for i in range(3):
            agent_value = random.randint(1, 800)
            agents.append(Agent(agent_value))

    return(agents)

def rate(agents):
  for agent in agents:
    agent.score = abs(goal - agent.condition)
    agent.color = int(255*(agent.score/800)), 0, 255 - int(255*(agent.score/800))

def display(agents, bestagnet):
    for agent in agents:
        pg.draw.ellipse(screen, (agent.color), pg.Rect(agent.condition, 400, 10, 10))
    pg.draw.ellipse(screen, (0, 255, 0), pg.Rect(bestagent.condition, 400, 10, 10))

def best(agents, bestagent):
    if bestagent == None:
        bestscore = 400
    else:
        bestscore = bestagent.score
    for agent in agents:
        if agent.score < bestscore:
            bestagent = agent
      #print("agent is destroyed: ",agent.score)
    return(bestagent)

# def cycle(cycles):
  
#   for i in range(1, cycles):
#     if i == 1:
#       agents = create(None, 1)
#     else:
#       agents = create(bestagent.condition, 1)
#     rate(agents)
#     bestagent = best(agents)
#     #print("best",bestagent.score, bestagent.condition)
#   return(bestagent.condition)


# print("the goal was",goal, "\n","after",cycles,"cycles, the closest agent was",cycle(cycles))

cycles = 100
i = 0
bestagent = None
while 1:
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(0, 0, 800, 800))
    i=i+1
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    #numberline
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(0, 392.5, 800, 5))

  
    if i == 1:
        agents = create(None, 1)
    else:
          agents = create(bestagent.condition, 1)
    rate(agents)
    bestagent = best(agents, bestagent)
    display(agents, bestagent)
    

        #print("best",bestagent.score, bestagent.condition)
    


    #pg.draw.ellipse(screen, (255, 10, 10), pg.Rect(30, 30, 60, 60))

    # screen.fill(black)
    pg.draw.rect(screen, (0, 0, 255), pg.Rect(goal, 390, 10, 10))
    pg.display.flip()
    pg.time.delay(1000)
    print(bestagent.condition, bestagent.score)