import pygame 
import gamesprite
class Player(gamesprite.GameSprite):

    ''' Simple player class which allows you to move
        a sprite across the screen with the arrow keys
    '''

    def __init__(self, filename, position, world_dim, *groups):

        ''' Initializes the player sprite '''
        super(Player, self).__init__(filename, position, world_dim, *groups)

    def update(self):

        ''' Moves the player sprite across the screen
            with arrow keys
        '''
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 10
        if key[pygame.K_RIGHT]:
            self.rect.x += 10
        if key[pygame.K_UP]:
            self.rect.y -= 10
        if key[pygame.K_DOWN]:
            self.rect.y += 10

        if self.rect.x + self.rect.width > self.world_dim[0]:
            self.rect.x = self.world_dim[0] - self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y + self.rect.height > self.world_dim[1]:           
            self.rect.y = self.world_dim[1] - self.rect.height
        if self.rect.y < 0:
            self.rect.y = 0

