import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from asteroid import Asteroid
from shot import Shot


def main():
    # Initialization code prior to game loop:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    # Game Loop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))

        clock.tick(60)
        dt = clock.get_time() / 1000
        #dt = clock.tick(60) / 1000

        for sprite in updatable:
            sprite.update(dt)
        #player.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)
        #player.draw(screen)

        pygame.display.flip()
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
if __name__ == "__main__":
    main()