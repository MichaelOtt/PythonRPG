import pygame 
import armor
import sword
import item
import utils.messagemanager
import utils.message
class Inventory(object):


    def __init__(self, screensize, player):
        self.open = False
        self.rows = 6
        self.cols = 10
        self.squareside = 50
        self.squareedge = 2.5
        self.screensize = screensize
        self.rect = pygame.Rect((screensize[0]-self.cols*self.squareside)/2,(screensize[1]-self.rows*self.squareside)/2,self.cols*self.squareside,self.rows*self.squareside)
        self.items = []
        self.equippedweapon = None
        self.equippedarmor = None
        self.createImage()
        self.rightClickDown = False
        '''self.image = pygame.image.load("filename")'''
        '''self.image = pygame.transform.scale(self.image, (self.rect.width,self.rect.height))'''
        self.player = player
    def addItem(self, item):
        self.items.append(item)
        self.createImage()
    def removeItem(self, item):
        if isinstance(item,sword.Sword):
            if self.equippedweapon == item:
                self.equippedweapon = None
        if isinstance(item,armor.Armor):
            if self.equippedarmor == item:
                self.equippedarmor = None
                self.player.maxhealth = 100
                self.player.reduction = 0
                self.player.heal(0)
        self.items.remove(item)
        self.createImage()
    def equipItem(self, index):
        item = self.items[index]
        if isinstance(item,sword.Sword):
            self.equippedweapon = item
        if isinstance(item,armor.Armor):
            self.equippedarmor = item
            self.player.maxhealth = 100+self.equippedarmor.health
            self.player.reduction = self.equippedarmor.reduction
            self.player.heal(0)
        self.createImage()
    def inventoryInteractions(self):
        mx,my = pygame.mouse.get_pos()
        index = self.getSlot(mx,my)
        if (index is not None) and (index < len(self.items)):
            self.displayStats(index,mx,my)
            m1,_,m3 = pygame.mouse.get_pressed()
            if not m3:
                self.rightClickDown = False
            if m1:
                self.equipItem(index)
            if m3 and self.rightClickDown == False:
                self.rightClickDown = True
                self.removeItem(self.items[index])
    def displayStats(self, index, x, y):
        item = self.items[index]
        lines = item.stats
        temprect = pygame.Rect(x,y,300,item.linenum*40)
        tempmessagebox = utils.messagemanager.createmessage(lines, temprect)
        tempmessage = utils.message.Message(tempmessagebox,temprect)
        utils.messagemanager.addabsolutemessage("weaponmessage",tempmessage)
    def displayInventory(self, screen):
        if self.open:
            screen.blit(self.image,self.rect)
    def createImage(self):
        temprect = pygame.Rect(0,0,self.squareside-self.squareedge*2, self.squareside-self.squareedge*2)
        self.image = pygame.Surface((self.rect.width,self.rect.height))
        pygame.draw.rect(self.image, (255,0,0), (0,0,self.rect.width,self.rect.height))
        '''self.image.blit(self.image,self.rect)'''
        for r in range(self.rows):
            for c in range(self.cols):
                temprect.x = c*self.squareside+self.squareedge
                temprect.y = r*self.squareside+self.squareedge
                pygame.draw.rect(self.image, (0,0,255), temprect)
        for tempitem in self.items:
            index = self.items.index(tempitem)
            row, col = self.findRowCol(index)
            tempimage = pygame.transform.scale(tempitem.image, (temprect.width, temprect.height))
            temprect.x = col*self.squareside+self.squareedge
            temprect.y = row*self.squareside+self.squareedge
            if tempitem == self.equippedweapon:
                pygame.draw.rect(self.image, (0,255,0), (col*self.squareside, row*self.squareside, self.squareside, self.squareside))
            if tempitem == self.equippedarmor:
                pygame.draw.rect(self.image, (255,255,0), (col*self.squareside, row*self.squareside, self.squareside, self.squareside))
            self.image.blit(tempimage, temprect)
    def findRowCol(self, index):
        row = (int)(index/self.cols)
        col = index % self.cols
        return row, col
    def getSlot(self, x, y):
        tempx = x-self.rect.x
        tempy = y-self.rect.y
        col = (int)(tempx/self.squareside)
        row = (int)(tempy/self.squareside)
        if (row < 0 or col < 0 or row >= self.rows or col >= self.cols):
            return None
        index = row*self.cols+col
        return index
