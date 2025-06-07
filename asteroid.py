import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x, y, radius):
        super().__init__(x,y,radius)
    
    #override draw
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, 2)
        
    def update(self,dt):
        self.position += self.velocity * dt
        
    #astroid splitting
    def split(self):
        self.kill() #immediately kill itself
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            #spawn into two asteroids if shot by the bullet
            #the split asteroids must move in new random directions
            random_angle = random.uniform(20,50) #generates a random angle between them
            
            #2 new splits from the random angle
            splitNew1 = self.velocity.rotate(random_angle)
            splitNew2 = self.velocity.rotate(-random_angle)
            
            #compute new radius of the 2 split asteroids
            newradius= self.radius - ASTEROID_MIN_RADIUS
            
            #create 2 new asteroid obj
            splitAsteroid1= Asteroid(self.position.x,self.position.y,newradius)
            splitAsteroid1.velocity = splitNew1 * 1.2
            
            splitAsteroid2 = Asteroid(self.position.x,self.position.y, newradius)
            splitAsteroid2.velocity = splitNew2 * 1.2
            
            
    """ with split method:
                    Large asteroids split into two medium asteroids
                    Medium asteroids split into two small asteroids
                    Small asteroids disappear when destroyed
    
    """