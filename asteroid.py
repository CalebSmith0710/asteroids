from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        positive_vector = self.velocity.rotate(angle)
        negative_vector = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(x = self.position[0], y = self.position[1], radius = new_radius)
        asteroid_2 = Asteroid(x = self.position[0], y = self.position[1], radius = new_radius)
        asteroid_1.velocity = positive_vector * 1.2
        asteroid_2.velocity = negative_vector * 1.2