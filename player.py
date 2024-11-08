from circleshape import CircleShape
from constants import PLAYER_RADIUS
import pygame
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from shot import Shot
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.timer = 0

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
        if self.timer > 0:
            self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Negative dt for counterclockwise rotation
        if keys[pygame.K_d]:
            self.rotate(dt)   # Positive dt for clockwise rotation
        if keys[pygame.K_w]:
            self.move(-dt)  # Negative dt for moving ship
        if keys[pygame.K_s]:
            self.move(dt)   # Positive dt for moving ship
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        #Check if player cannot shoot
        if self.timer > 0:
            return
    
        # Set the cooldown timer
        self.timer = PLAYER_SHOOT_COOLDOWN

        # Create the shot at the player's current position
        new_shot = Shot(self.position.x, self.position.y)
        
        # Set the shot's velocity
        direction_vector = pygame.Vector2(0, -1)  # Adjust to initial default direction
        shot_velocity = direction_vector.rotate(self.rotation) * PLAYER_SHOOT_SPEED
        new_shot.velocity = shot_velocity
        
        # Add the shot to the shots group
        self.shots_group.add(new_shot)

    def main():
        # Screen dimensions
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        # Create the shots group
        shots_group = pygame.sprite.Group()

        # Calculate the initial position
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2

        # Create a player instance
        player = Player(x, y, shots_group)

        # Rest of your game loop and logic
        # ...

        # Example of updating and drawing shots
        shots_group.update()
        for shot in shots_group:
            shot.draw(screen)  # Assuming Shot class has a draw method

        # Don't forget to display text and finalize running conditions
