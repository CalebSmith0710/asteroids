# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroidfield import *
from asteroid import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for obj in asteroids:
            if obj.collides(player):
                print("Game over!")
                sys.exit()

        screen.fill(color=(0, 0, 0))
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
