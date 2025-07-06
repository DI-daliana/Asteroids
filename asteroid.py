from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self,x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,'white', self.position , self.radius, width=2)
    
    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20 , 50)
            
            random_angle1 = pygame.Vector2(self.velocity).rotate(angle)
            random_angle2 = pygame.Vector2(self.velocity).rotate(-angle)


            new_radius = self.radius - ASTEROID_MIN_RADIUS

            ast1= Asteroid(self.position.x, self.position.y, new_radius)
            ast2= Asteroid(self.position.x, self.position.y, new_radius)


            ast1.velocity=random_angle1 *1.2
            ast2.velocity=random_angle2 *1.2
            

            
