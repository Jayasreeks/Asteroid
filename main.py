import pygame
from constants import *
from player import Player # player is a module and Player is the class inside it so importing only the class 


def main():
    pygame.init()
    
    # this will create the pop up display screen 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    
    clock = pygame.time.Clock()
    dt=0
    
    updatable=pygame.sprite.Group() # all obj that need update 
    drawable=pygame.sprite.Group() # all obj tht need drawing 
    
    # adding groups as containers to the player class
    Player.containers=(updatable,drawable)# containers- class variable of Player class 
    
    # drawing the player after the screen appears and b4 flipping the screen
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # creating player pbject before loop 
    
    
    #game loop starts
    running= True
    while running:
        for event in pygame.event.get(): # will get all the events from the screen 
            if event.type == pygame.QUIT:
                running = False
                
        #code b4 adding groups
        """#update player state
        player1.update(dt)
        
        #render everything from here        
        screen.fill(color="black")
        player1.draw(screen)
        pygame.display.flip() 
        """
        screen.fill(color="black")
        updatable.update(dt) # updates all obj in the updatable groups
        
        #draw all obj in the drawable group 
        for obj in drawable:
            obj.draw(screen)
        
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
    

