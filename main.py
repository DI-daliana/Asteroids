# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from Shot import *

def main():
    pygame.get_init()
    
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    AsteroidField.containers =(updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots,updatable, drawable)
    
    asteroid = AsteroidField()
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    while game==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = clock.tick(60)/1000
        
        screen.fill((0,0,0))
        for p in drawable:
            p.draw(screen)

        for p in updatable:
            p.update(dt)

        for ast in asteroids:
            if ast.collisions(player) == True:
                sys.exit("Game Over") 
        
        for at in asteroids:
            for sh in shots:
                if at.collisions(sh)==True:
                    at.split()
                    pygame.sprite.Sprite.kill(sh)
        pygame.display.flip()
        
    

if __name__ == "__main__":
    main()