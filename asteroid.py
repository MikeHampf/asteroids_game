from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_position_x = self.position.x
        old_position_y = self.position.y
        old_radius = self.radius
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        vector_1 = self.velocity.rotate(rand_angle)
        vector_2 = self.velocity.rotate(-rand_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(old_position_x, old_position_y, new_radius)
        new_asteroid_2 = Asteroid(old_position_x, old_position_y, new_radius)
        new_asteroid_1.velocity = vector_1
        new_asteroid_2.velocity = vector_2
