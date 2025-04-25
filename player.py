from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    
    rotation = 0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
     
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        self.move(dt)
        # if keys[pygame.K_UP] or keys[pygame.K_w]:
        #     forward = pygame.Vector2(0, -1).rotate(self.rotation)
        #     self.velocity += forward * PLAYER_SPEED * dt
        # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        #     # Deceleration
        #     forward = pygame.Vector2(0, -1).rotate(self.rotation)
        #     self.velocity -= forward * PLAYER_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
