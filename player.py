from circleshape import CircleShape
from constants import PLAYER_RADIUS
import pygame
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Negative dt for counterclockwise rotation
        if keys[pygame.K_d]:
            self.rotate(dt)   # Positive dt for clockwise rotation
        if keys[pygame.K_w]:
            self.move(-dt)  # Negative dt for moving ship
        if keys[pygame.K_s]:
            self.move(dt)   # Positive dt for moving ship

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

def main():
    #Screen dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    #Calculate the initiasl position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #Player instance
    player = Player(x, y)
