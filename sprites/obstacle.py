import pygame 
import gamesprite
import utils.soundplayer
class Obstacle(gamesprite.GameSprite):

    ''' Simple object that moves left and right across the screen '''

    def __init__(self, filename, position, world_dim, rectangle, *groups):

        ''' Initializes the obstacle sprite '''

        super(Obstacle, self).__init__(filename, position, world_dim, rectangle, *groups)
         
    def update(self,game_sprites,soundplayer):
        pass
        ''' Changes the direction of the sprite if it hits the edge of the screen '''

