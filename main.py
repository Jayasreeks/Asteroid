import pygame
from constants import *

def main():
    pygame.init()
    
    # this will create the pop up display screen 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    
    clock = pygame.time.Clock()
    dt=0
    
    running= True
    while running:
        for event in pygame.event.get(): # will get all the events from the screen 
            if event.type == pygame.QUIT:
                running = False
        screen.fill(color="black")
        pygame.display.flip() 
        
        dt=clock.tick(60)/1000 #Calculate delta time at the end
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":       
    main()
    """
This line ensures the main() function is only called when this
file is run directly; it won't run if it's imported as a module.
It's considered the "pythonic" way to structure an executable program
in Python.


    """
    

