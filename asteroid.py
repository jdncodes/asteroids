import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        points_earned = 0

        if self.radius <= ASTEROID_MIN_RADIUS:
            #Add player score logic, smallest = 1 point
            points_earned += 1
            return points_earned
        
        else:
        #Add player score logic for other asteroids
        points_earned += 10

        #Continuation of random angles & new asteroid production
        random_angle = random.uniform(20,50)

        new_dir_a = self.velocity.rotate(random_angle)
        new_dir_b = self.velocity.rotate(-random_angle)

        old_radius = self.radius
        new_smaller_radius = old_radius - ASTEROID_MIN_RADIUS

        new_asteroid_a = Asteroid(self.position.x, self.position.y, new_smaller_radius)
        new_asteroid_a.velocity = new_dir_a * 1.2
        new_asteroid_b = Asteroid(self.position.x, self.position.y, new_smaller_radius)
        new_asteroid_b.velocity = new_dir_b * 1.2

        '''
        asteroid = Asteroid(self.position.x, self.position.y, new_smaller_radius)
        asteroid.velocity = new_dir_a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_smaller_radius)
        asteroid.velocity = new_dir_b * 1.2
        '''
        #self.kill()
        return points_earned


        
        
        