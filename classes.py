import pygame
from pygame.locals import *
import time
import random

class RandomEnemy(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image #Bild muss bei Klassenzuweisung angegeben werden
        #Eben für das Bild
        self.surf = pygame.Surface((50, 62))
        #spawnt ein Rect random im vordefinierten Rechteck
        self.rect = self.surf.get_rect(center=(random.randrange(435, 510-25), random.randrange(191, 300-31)))

    def move(self):
        pass


#Gegner Klasse
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #erbt die Sprite Methoden
        # self.image = pygame.image.load("Grafiken\pikachu_trans.png").convert() #ruft Bild auf
        # self.image.set_colorkey((0,0,0))
        self.surf = pygame.Surface((50,62)) #erstellt eine Ebene für das Bild
        self.rect = self.surf.get_rect(center=(120,120) )#erstellt ein Rechteck um das Bild zum tracken und spawnt es an einer zufälligen Stelle im unten definierten Rechteck

    def move(self):
        pass
    #     self.rect.move_ip(0, 3)
    #     if (self.rect.top > 300): #überprüft, ob das Bild das untere Ende erreicht hat
    #         self.rect.top = 0 #setzt den Gegner wieder an den Anfang
    #         self.rect.center = (30,50)

#Spieler Klasse analog zu Gegner
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Grafiken\player.png")
        self.surf = pygame.Surface((50,50))
        self.rect = self.surf.get_rect(center=(150,150))

    def move(self):
        pressed_keys = pygame.key.get_pressed() #überprüft ob irgendwelche Tasten gedrückt werden

        #Wenn die definierte Taste gedrückt wird --> Bewegung um x Pixel in gedrückte Richtung
        if self.rect.top > 0:
            if pressed_keys[K_UP]: # >, < sorgt dafür, dass der Spieler den Screen nicht verlässt
                self.rect.move_ip(0,-5)

        if self.rect.bottom < 480:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

        if self.rect.right > 0 and self.rect.right < 640:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

        if self.rect.left < 640 and self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)