import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip() 
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
    

