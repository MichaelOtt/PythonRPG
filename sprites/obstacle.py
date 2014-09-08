import pygame 
import gamesprite
class Obstacle(gamesprite.GameSprite):

    ''' Simple object that moves left and right across the screen '''

    def __init__(self, filename, position, world_dim, *groups):

        ''' Initializes the obstacle sprite '''

        super(Obstacle, self).__init__(filename, position, world_dim, *groups)

        self.offset_x = 50
	self.offset_y = 20

         
    def update(self):

        ''' Changes the direction of the sprite if it hits the edge of the screen '''

        if self.rect.x + self.rect.width > self.world_dim[0] or self.rect.x < 0:
            self.offset_x *= -1
        if self.rect.y + self.rect.height > self.world_dim[1]:
            self.offset_y *= -1
            self.rect.y = self.world_dim[1] - self.rect.height
        if self.rect.y < 0:
            self.offset_y *= -1
            self.rect.y = 0
            
        self.offset_y += 5
        self.rect.x += self.offset_x
        self.rect.y += self.offset_y
        
