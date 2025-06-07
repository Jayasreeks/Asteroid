import pygame
from constants import *
from player import Player # player is a module and Player is the class inside it so importing only the class 


def main():
    pygame.init() #1.initializes all the imported pygame modules
    
    #2. this will create the pop up display screen 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    
    #7.creating an clock object to keep track of the time 
    clock = pygame.time.Clock()
    dt=0
    
    updatable=pygame.sprite.Group() # all obj that need update 
    drawable=pygame.sprite.Group() # all obj tht need drawing 
    
    #9.adding 2 groups as containers to the player class
    Player.containers=(updatable,drawable)# containers- class variable of Player class, can belong to both group at the same time
    
    #create variable after creating group
    #10. instantiate the player object - to spawn in the middle of the screen - 
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # creating player pbject before loop 
    
    
    #3.game loop starts
    running= True
    while running:
        #6. adding surface(screen) close event
        for event in pygame.event.get(): # will get all the events from the screen 
            if event.type == pygame.QUIT: # check if the user has closed the window..if yes exit the game loop and make the window's close button to work
                running = False
                
        #code b4 adding groups
        """#update player state
        player1.update(dt)
        
        #render everything from here        
        screen.fill(color="black")
        player1.draw(screen)
        pygame.display.flip() 
        """
        #4.set the surface color to balck 
        pygame.Surface.fill(screen,(23,25,93))
        #screen.fill(color="black") - can also be this way
        
        #11. call .update() method on the updatable group
        updatable.update(dt) # updates all obj in the updatable groups
        
        #12. draw all obj in the drawable group 
        for obj in drawable:
            obj.draw(screen)
            
        #5.refresh the surface screen 
        pygame.display.flip()
        
        #8. for calculating the amount of time that has passed since the last time it was called
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
    

