import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def check_collision(self, otherCircleShape):
        # this distacne_to method is used to calculate the distance between the two objects 
        distance = pygame.math.Vector2.distance_to(self.position,otherCircleShape.position) 
        
        #if the euclidian dist between the two obj is less than the sum of tis radius the they collide else not
        if(distance <= self.radius + otherCircleShape.radius):
            return True
        else:
            return False