import pygame as pg, sys

from pygame.constants import K_SPACE
pg.init()

size = width, height =  800, 800
speed = [2, 2]
black = 0, 0, 0
screen = pg.display.set_mode(size)

import random
import math
class Agent:
    def __init__(self, x, y):
      self.x = x
      self.y = y
      self.scorex = 0
      self.scorey=0
      self.score =0
      self.color = 0, 0, 0


goalx = random.randint(50,750)
goaly = random.randint(50, 750)

def create(previousx, previousy):
    agents=[]
    if previousx != None:
        for i in range (added_agents):
            agents.append(Agent(previousx - random.randint(-variation,variation), previousy - random.randint(-variation,variation)))
        agents.append(Agent(previousx, previousy))
    else:
        for i in range(og_agents):
            agents.append(Agent(random.randint(0, 800),random.randint(0, 800)))

    return(agents)

def rate(agents):
  for agent in agents:
    agent.scorex = abs(goalx - agent.x)
    agent.scorey = abs(goaly- agent.y)
    agent.score = int(math.sqrt(agent.scorex**2 + agent.scorey**2))
    agent.color = int(255*(agent.score/1132)), 0, 255 - int(255*(agent.score/1132))

def display(agents, bestagnet):
    for agent in agents:
        pg.draw.ellipse(screen, (agent.color), pg.Rect(agent.x, agent.y, 10, 10))
    pg.draw.ellipse(screen, (0, 255, 0), pg.Rect(bestagent.x, bestagent.y, 10, 10))

def best(agents):
    bestscore = 1300
    for agent in agents:
        if agent.score < bestscore:
            bestagent = agent
            bestscore = agent.score
      #print("agent is destroyed: ",agent.score)
    return(bestagent)

# def goalmove(goalx, goaly, speed):
#     if goalx<750-speed:
#         if goalx>50+speed:goalx = goalx + random.randint(-speed, speed)
#         else: goalx = goalx + random.randint(0, speed)
#     else:goalx = goalx - random.randint(0, speed)
#     if goaly<750-speed:
#         if goaly>50+speed:goaly = goaly + random.randint(-speed, speed)
#         else: goaly = goaly + random.randint(0, speed)
#     else:goaly = goaly - random.randint(0, speed)
#     return(goalx, goaly)

def goalmove(goalx, goaly, speedx, speedy, directionx, directiony):
    if goalx >=780:
        directionx = -1
    elif goalx <= 20:
        directionx = 1
    
    if goaly >=780:
        directiony = -1
    elif goaly <= 20:
        directiony = 1
    goalx = goalx + speedx*directionx
    goaly = goaly + speedy*directiony
    return(goalx, goaly, directionx, directiony)

def chart_locations(locations):
    for i in range(int(len(locations)/3)):
        pg.draw.ellipse(screen,(50, 50, 50), pg.Rect(locations[i*3][0],locations[i*3][1], 10, 10))



speedx = 8
speedy = 15
og_agents = 1
added_agents = 6
variation = 3


locations =[]
cycles = 100
i = 0
bestagent = None
directionx, directiony = 1, 1
while 1:
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(0, 0, 800, 800))
    i=i+1
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    #numberline
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(0, 392.5, 800, 5))

  
    if i == 1:
        agents = create(None, None)
    else:
        agents = create(bestagent.x, bestagent.y)
    rate(agents)
    bestagent = best(agents)
    display(agents, bestagent)


    locations.append([bestagent.x, bestagent.y, bestagent.score])
    chart_locations(locations)

    averagedistance = 0
    for location in locations:
        averagedistance += location[2]
    averagedistance = int(averagedistance/len(locations))

        #print("best",bestagent.score, bestagent.condition)
    font = pg.font.SysFont(None, 24)
    img = font.render('Average distance: '+str(averagedistance), True, (255, 255, 255))
    screen.blit(img, (20, 20))


    #pg.draw.ellipse(screen, (255, 10, 10), pg.Rect(30, 30, 60, 60))

    # screen.fill(black)
    pg.draw.rect(screen, (0, 0, 255), pg.Rect(goalx, goaly, 10, 10))
    pg.display.flip()
    pg.time.delay(10)
    print(bestagent.x, bestagent.y, bestagent.score)
    goalx, goaly, directionx, directiony = goalmove(goalx, goaly, speedx, speedy,directionx, directiony)

    keys=pg.key.get_pressed()
    if keys[K_SPACE]:
        quit()



    #idea: it could be able to predict motion by take 3 data points, finding the first difference, if its constant finding the next point, and if it is not getting another datapoint and calculating the next difference.