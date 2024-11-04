import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        # Initialize parent class with SHOT_RADIUS
        super().__init__(x, y, SHOT_RADIUS)
        
        # Set position
        self.position = pygame.math.Vector2(x, y)
        
        # Initialize other necessary properties, like velocity
        self.velocity = pygame.math.Vector2(0, 0)  # Placeholder initialization

         # Create a simple surface for the shot's image
        self.image = pygame.Surface((SHOT_RADIUS*2, SHOT_RADIUS*2), pygame.SRCALPHA)
        
        # Draw a circle on this surface
        pygame.draw.circle(self.image, "white", (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)
        
        # Create a rect for positioning and collision
        self.rect = self.image.get_rect(center=self.position)

    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt
        # Update the rectangle position
        self.rect.center = self.position