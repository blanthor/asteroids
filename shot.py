from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.rotation_speed = 0.5  # degrees per second
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, SHOT_RADIUS)

    def update(self, dt):
        super().update(dt)
        self.position += self.velocity * dt
