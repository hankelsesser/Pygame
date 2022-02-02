import pygame, sys, random
pygame.init()

size = width, height =  800, 800
black = 0, 0, 0

screen = pygame.display.set_mode(size)



class Spark:
    def __init__(self, x, y, xvelocity, yvelocity):
        self.x = x
        self.y = y
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity

sparks = [Spark(width/2, height-(height/3), 0, 50)]

def firework(coords):
    pass

def draw(sparks):
    for spark in sparks:
        pygame.draw.ellipse(screen,(255, 255, 255), pygame.Rect(spark.x, spark.y, 10, 10))

def move(sparks):
    for spark in sparks:
        spark.x += (spark.xvelocity/200)
        spark.y -= (spark.yvelocity/200)
        if spark.yvelocity > -5:
            spark.yvelocity -= 0.025
    #spark.yvelocity -= 
        

def explode(sparks):
    new_sparks = sparks
    for n in range(len(sparks)):
        #print("hi")
        new_sparks.append(sparks[n])
        new_sparks.append(Spark(sparks[n].x, sparks[n].y, sparks[n].xvelocity + random.randint(5, 10), sparks[n].yvelocity +random.randint(5, 10)))
        new_sparks.append(Spark(sparks[n].x, sparks[n].y, sparks[n].xvelocity + random.randint(5, 10), sparks[n].yvelocity -random.randint(5, 10)))
        new_sparks.append(Spark(sparks[n].x, sparks[n].y, sparks[n].xvelocity - random.randint(5, 10), sparks[n].yvelocity +random.randint(5, 10)))
        new_sparks.append(Spark(sparks[n].x, sparks[n].y, sparks[n].xvelocity - random.randint(5, 10), sparks[n].yvelocity -random.randint(5, 10)))
    return(new_sparks)

round = 0
while 1:
    round += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    if round % 250 == 0 and round > 900 and round < 1700:
        print(len(sparks))
        sparks = explode(sparks)
    draw(sparks)
    move(sparks)
    
    pygame.display.flip()