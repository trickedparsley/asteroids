import random
import pygame
from circleshape import *
from constants import *
from logger import log_event

# Base class for game objects
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")
            offset = random.uniform(20, 50)
            fo = self.velocity.rotate(offset)
            so = self.velocity.rotate(-offset)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first = Asteroid(self.position.x, self.position.y, new_radius)
            second = Asteroid(self.position.x, self.position.y, new_radius)
            first.velocity = fo * 1.2
            second.velocity = so * 1.2