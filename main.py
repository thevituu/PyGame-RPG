import pygame
from pygame.locals import *
import time
import random
import sys
sys.path.append("E:\zDavid\Python\PyGameTutorial")
from classes import *

pygame.init()

#Farben
BLUE = (0,0,255)
WHITE = (255, 255, 255)
GREY = (125,125,125)

#erstellen eines Fensters mit Auflösung
DISPLAYSURF = pygame.display.set_mode((640, 480))
DISPLAYSURF.fill(WHITE)

#FPS und Titenl einstellen
FPS = pygame.time.Clock()
pygame.display.set_caption("tbd")




#bei Begegnung mit Gegner KampfUI aufrufen
def fight_ui(player, enemy):
    fight_ui.has_been_called = True #zum überprüfen, ob fight_ui ausgeführt wurde
    #Ändert Hintergrund in KampfUI
    DISPLAYSURF.blit(fight_bg, (0,0))
    #platziert Gegner und Spieler auf Position
    player.rect = player.surf.get_rect(center=(150,220))
    enemy.rect = enemy.surf.get_rect(center=(450,220))
#Standardmäßig ist das fight_ui deaktiviert
fight_ui.has_been_called = False



bg = pygame.image.load("Grafiken\hintergrund.png")
fight_bg = pygame.image.load("Grafiken\kampf_bg.png")


#Rechteckt, indem zufällige Encounter gespawnt werden
rect = pygame.draw.rect(bg, BLUE, (410,160,100,140), 2)


#Definition von Spieler und Gegner
#RandomEnemy(GegnerSprite)
E1 = RandomEnemy(pygame.image.load("Grafiken\pikachu_trans.png"))
P1 = Player()

#Sprite Groups
enemies = pygame.sprite.Group() #erstellen einer Sprite Group für Gegner
enemies.add(E1)
all_sprites = pygame.sprite.Group() #erstellen einer sprite group für alles
all_sprites.add(P1)

while True:
    for event in pygame.event.get(): #schaut nach Events, die gerade im Spiel stattfinden
        if event.type == QUIT: #type QUIT sagt aus, dass das Spiel geschlossen wird oder nicht
            pygame.quit()
            sys.exit()

    #überprüft, ob Spieler bereits im Kampf ist, wenn nicht: Open World laufen
    if fight_ui.has_been_called == False:
        P1.move() #schaut, ob Bewegungseingaben ankamen
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(bg, (0,0))

    #redraw sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)

    #zeichnet die Sprites der Zufallsbegegnungen erst wenn es zu einem Kampf kommt
    if fight_ui.has_been_called == True:
        for entity in enemies:
            DISPLAYSURF.blit(entity.image, entity.rect)

    #überprüfen ob Spieler mit Gegner sprite kollidiert und ruft anschließend den Kampf und die KampfUI auf
    if pygame.sprite.spritecollideany(P1, enemies):
        for entity in enemies:
            fight_ui(P1, entity)
        pygame.display.update() #refresh Display
        # for entity in all_sprites:
        #     entity.kill() #entfernt alle sprites

    #Verlassen des Spiels bei Drücken der ESC Taste
    quit_key = pygame.key.get_pressed()
    if quit_key[K_ESCAPE]:
        pygame.quit()
        sys.exit()


    pygame.display.update() #aktualisiert Änderungen im Spiel
    FPS.tick(30)



