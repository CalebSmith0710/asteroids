from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0, 1).rotate(rotation)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius)

    def update(self, dt):
        self.position += self.velocity * dt * PLAYER_SHOT_SPEED

    def rotate(self, rotation):
        self.rotation += rotation