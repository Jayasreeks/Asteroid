import pygame

from constants import *
from circleshape import CircleShape
from shot import Shot
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y,PLAYER_RADIUS)
        self.rotation=0
        self.shoot_timer = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen, "white",self.triangle(),3)
        
        
    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # roate left
            self.rotate(-dt)
        if keys[pygame.K_d]: # rotate right
            self.rotate(dt)
        if keys[pygame.K_w]: # move forward
            self.move(dt)
        if keys[pygame.K_s]: # move backward
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            
    def rotate(self,dt): # this roate is diff from pygame.vector.rotate() function- this one here is custom func
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    #after shot class
    def shoot(self):
        if(self.shoot_timer > 0):
            return
        # when the player shoots set the timer to new const
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x,self.position.y)
        direction = pygame.Vector2(0,1).rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED
        
        
            
    
    
        