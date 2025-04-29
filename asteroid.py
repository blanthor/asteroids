import pygame
from circleshape import CircleShape
from constants import *
import random 


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.rotation_speed = 0.5  # degrees per second

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        super().update(dt)
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(self.radius < ASTEROID_MIN_RADIUS):
            return
        split_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(split_angle)
        velocity2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2


