# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

pygame.init()

clock = pygame.time.Clock() 
dt = 0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # This gives us dt in seconds

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

        # Render
        screen.fill((0, 0, 0))  # Clear the screen

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()






 

if __name__ == "__main__":
    main()
