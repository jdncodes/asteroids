import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from asteroid import Asteroid
from shot import Shot

'''
#Add Score Counter on the top left
#player_score = 0
#Add font for the score diplay
#game_font = pygame.font.Font(None, SCORE_FONT_SIZE)
'''#Look into this later

def main():
    # Initialization code prior to game loop:
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Add score counter on the top left:
    player_score = 0

    #Add font for the score diplay
    game_font = pygame.font.Font(None, SCORE_FONT_SIZE)

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

    '''#Add Score Counter on the top left
    #player_score = 0
    #Add font for the score diplay
    #game_font = pygame.font.Font(None, SCORE_FONT_SIZE)''' #Look into this later

    # Game Loop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("=================")
                print(f"Your session's score: {player_score}")
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
                print("=================")
                print(f"Your session's score: {player_score}")
                sys.exit()
                return

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides(shot):
                    player_score += asteroid.split()  #Adds points_earned local var to player_score func var
                    shot.kill()
                    #Maybe add this for debugging in console:
                    # points = asteroid.split()
                    # player_score += points
                    # print(f"Got {points} points from asteroid!")

        for sprite in drawable:
            sprite.draw(screen)
        #player.draw(screen)

        #Add rendering the score text:
        score_text = game_font.render(f"Score: {player_score}", True, SCORE_COLOR)
        #Drawing the score onto the screen so its visible:
        screen.blit(score_text, SCORE_POSITION)

        pygame.display.flip()
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
if __name__ == "__main__":
    main()