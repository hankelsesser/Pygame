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


def rate(agent):
    agent.scorex = goalx - agent.x
    agent.scorey = goaly- agent.y
    agent.score = int(math.sqrt(agent.scorex**2 + agent.scorey**2))
    agent.color = int(255*(agent.score/1132)), 0, 255 - int(255*(agent.score/1132))


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

def predict(goaldistances, locations):
    if len(goaldistances) < 3:
        x=0
        print("calculating")
    else:
        changea = goaldistances[-1][0] 
        changeb = goaldistances[-2][0]
        a = locations[-1][0]
        b = locations[-2][0]
        loca = a+changea
        locb= b+changeb
        x= loca+(loca-locb)

    if len(goaldistances) < 3:
        y=0
    else:
        changea = goaldistances[-1][1] 
        changeb = goaldistances[-2][1]
        a = locations[-1][1]
        b = locations[-2][1]
        loca = a+changea
        locb= b+changeb
        y= loca+(loca-locb)
    return(x, y)
            



speedx = random.randint(5,10)
speedy = random.randint(6, 11)
goaldistances=[]
locations =[]
i = 0
directionx, directiony = 1, 1
agent = Agent(400, 400)

while 1:
    pg.draw.rect(screen, (0, 0, 0), pg.Rect(0, 0, 800, 800))
    i=i+1
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    rate(agent)
    goaldistances.append([agent.scorex, agent.scorey])
    agent.x, agent.y = predict(goaldistances, locations)

    pg.draw.ellipse(screen, (255, 0 ,0), pg.Rect(agent.x, agent.y, 10, 10))



    locations.append([agent.x, agent.y, agent.score])

    chart_locations(locations)

    averagedistance = 0
    for location in locations:
        averagedistance += location[2]
    averagedistance = int(averagedistance/len(locations))


    font = pg.font.SysFont(None, 24)
    img = font.render('Average distance: '+str(averagedistance), True, (255, 255, 255))
    screen.blit(img, (20, 20))



    pg.draw.rect(screen, (0, 0, 255), pg.Rect(goalx, goaly, 10, 10))
    pg.display.flip()
    pg.time.delay(10)
    goalx, goaly, directionx, directiony = goalmove(goalx, goaly, speedx, speedy,directionx, directiony)

    keys=pg.key.get_pressed()
    if keys[K_SPACE]:
        quit()



    #idea: it could be able to predict motion by take 3 data points, finding the first difference, if its constant finding the next point, and if it is not getting another datapoint and calculating the next difference.