import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.mana = 10
        self.speed = 3
    def choose_attack(self, enemy): #Kampf-Handlungsauswahl
        x = input("Was möchtest du tun?\n [1] " + "Faustschlag" +   " [2] " + "Steinwurf" + "\n ")
        if x == "1":
            spieler.attack_1(enemy)
        elif x == "2":
            spieler.attack_2(enemy)
        else:
            print("Bist du zu dumm eine der vorgegebenen Zahlen zu drücken? Auf jetzt, probiers nochmal!") #hier später einfügen, dass wenn dreimal eine fehlerhafte Antwort eingegeben wird, irgendwas passiert
            spieler.choose_attack(enemy)
    def attack_1(self, enemy): #Attacke 1
        enemy.health -= 1
        print("%s rennt auf den Gegner zu und haut ihm seine Faust ins Maul und fügt ihm 1 Schaden zu." %spieler.name)
    def attack_2(self, enemy): #Attacke 2
        enemy.health -= 3
        print("%s wirft wie behindert mit Steinen um sich und fügt ihm 3 Schaden zu." %spieler.name)




class PlayerLogic:
    def __init__(self, name, max_health, mana, crit, attacks):
        self.name = name
        self.level = 1
        self.max_exp = int((self.level * 22)**(1.5)*0.5)
        self.current_exp = 0
        self.max_health = max_health
        self.mana = mana
        self.crit = crit
        self.attacks = attacks

    def choose_attack(self, enemy): #Kampf-Handlungsauswahl
        x = input("Was möchtest du tun?\n [1] " + self.attacks[1].name + " [2] " + self.attacks[2].name + "\n ")
        if x == "1" or x == "2":
            return int(x)
        else:
            print("Bist du zu dumm eine der vorgegebenen Zahlen zu drücken? Auf jetzt, probiers nochmal!") #hier später einfügen, dass wenn dreimal eine fehlerhafte Antwort eingegeben wird, irgendwas passiert
            spieler.choose_attack(enemy)

    def attack(self, enemy, x): #Attacke 1
        damage = self.attacks[x].damage
        genauigkeit = round(random.uniform(0,1),2)
        if genauigkeit > self.attacks[x].accuracy: #überprüft, ob der Angriff trifft oder daneben geht
            print("Der Angriff ging daneben, du Lappen.")
        else:
            if PlayerLogic.func_crit(self) == True:
                damage = 2 * damage
                print(self.attacks[x].angriffstext + " Kritischer Treffer!")
            else:
                print(self.attacks[x].angriffstext)
            enemy.health -= damage
            if self.attacks[x].kategorie == "lebensraub":                                   #TODO: Maximale Lebensgrenze zwar gemacht, aber beobachten, ob es so funktioniert, weil kinda sus
                lifesteal = 0.5 * damage
                if self.health + lifesteal >= self.max_health: #überprüfen ob aktuelle HP + Lifesteal nicht über maximales Leben hinausgeht
                    self.health = self.max_health
                else:
                    self.health += lifesteal
                print("%s hat sich um %s Lebenspunkte geheilt." % (self.name, str(lifesteal)))

    def func_crit(self):
        critical = round(random.uniform(0, 1),2)
        if critical <= self.crit:
            return True

    def level_up(self):
        self.level += 1
        self.max_exp=(self.level * 22) ** (1.5) * 0.3 #Exponentielle EXP-Steigerung







class Enemy():
    def __init__(self, name, level, health, damage, speed, crit, attacks):
        self.name = name
        self.level = level
        self.exp = int((self.level * 22)**(1.5)*0.04) #EXP, die bei Sieg an den Spieler gegeben wird
        self.health = health
        self.damage = damage
        self.speed = speed
        self.crit = crit
        self.attacks = attacks

    def attack(self, spieler):
        which_attack = random.randint(1, 2)
        damage = self.attacks[which_attack].damage
        genauigkeit = round(random.uniform(0, 1), 2)
        if genauigkeit > self.attacks[which_attack].accuracy:  # überprüft, ob der Angriff trifft oder daneben geht
            print("Der Angriff von %s ging daneben." % (self.name))
        else:
            if Enemy.func_crit(self) == True:
                damage = 2 * damage
                print(self.attacks[which_attack].angriffstext + " Kritischer Treffer!")
            else:
                print(self.attacks[which_attack].angriffstext)
            spieler.health -= damage
            if self.attacks[which_attack].kategorie == "lebensraub":
                lifesteal = 0.5 * damage
                self.health += lifesteal
                print("%s hat sich um %s Lebenspunkte geheilt." % (self.name, str(lifesteal)))

    def func_crit(self):
        critical = round(random.uniform(0, 1),2)
        if critical <= self.crit:
            return True








class Warrior(PlayerLogic):
    def __init__(self, name, attacks):
        PlayerLogic.__init__(self, name=name, max_health=13, mana=10, crit=0.3, attacks=attacks)
        self.health = self.max_health
        self.speed = 5

class Mage(PlayerLogic):
    def __init__(self, name, attacks):
        PlayerLogic.__init__(self, name=name, max_health=10, mana=20, crit=0.15, attacks=attacks)
        self.health = self.max_health
        self.speed = 3






class Attacken:
    def __init__(self, name, damage, mana_cost, accuracy, kategorie, angriffstext):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.accuracy = accuracy
        self.kategorie = kategorie
        self.angriffstext = angriffstext











def fight(player, enemy):  #Kampfablauf 1v1 unter Berücksichtigung von Speed
    while enemy.health > 0 and player.health > 0:
        print(enemy.name + "'s HP: " + str(enemy.health))
        print(player.name + "'s HP: " + str(player.health) + "\n")
        chosen_attack = spieler.choose_attack(enemy) #Auswahl der auszuführenden Attacke des Spielers

        if enemy.speed < player.speed:
            spieler.attack(enemy, chosen_attack)
            wait()
            if enemy.health > 0:
                enemy.attack(player)
                wait()
        elif enemy.speed > player.speed:
            enemy.attack(player)
            wait()
            if player.health > 0:
                spieler.attack(enemy, chosen_attack)
                wait()
        else: #Falls Geschwindigkeiten gleich sind, zufällige Entscheidung, wer zuerst angreift
            rand_var = random.randint(1,2)
            if rand_var == 1:
                spieler.attack(enemy, chosen_attack)
                wait()
                if enemy.health > 0:
                    enemy.attack(player)
                    wait()
            else:
                enemy.attack(player)
                wait()
                if player.health > 0:
                    spieler.attack(enemy, chosen_attack)
                    wait()
        if player.health <= 0:
            print("Du bist gestorben.")
        elif enemy.health <= 0:
            player.current_exp += enemy.exp
            if player.current_exp >= player.max_exp:
                z = player.current_exp - player.max_exp #berechnet überschüssige EXP nach level up
                player.level_up()
                player.current_exp = 0 + z #fügt überschüssige EXP zum neuen Level hinzu
            print("Der Gegner ist gestorben.")




def wait(): #Hierfür bei Start des Spiels darauf aufmerksam machen, dass bei dem Zeichen ">" Enter zu drücken ist
    input(">\n")




spieler = Player(input("Wie heißt du? "))






print(spieler.name + " öffnet seine Augen und sieht sich um. Ehe er sich versieht, wird er von einem hässlichen Warzenschwein angegegriffen.\n")
time.sleep(0.5)


#Gegnerattacken
beissen = Attacken("Beißen", 2, 0, 0.9, "schaden", "Der Gegner rennt auf %s zu und beißt ihm in die Hand." %(spieler.name))
ueberrennen = Attacken("Überrennen", 4, 0, 0.9, "schaden", "Der Gegner überrennt %s." %spieler.name)
schwein = Enemy("hässliches Warzenschwein", 1, 5, 6, 2, 0.2, {1: beissen, 2: ueberrennen})

#Attacken
#Warrior
schwerthieb = Attacken("Schwerthieb", 5, 0, 0.9, "schaden", "%s rennt mit seinem Schwert los und fügt dem Gegner einen gewaltigen Schwerthieb zu." %(spieler.name))
schwertwirbel = Attacken("Schwertwirbel", 3, 0, 0.8, "schaden", "%s zückt seine Klinge und führt einen schnellen Schwertwirbel aus." %spieler.name)

#Mage
energieschuss = Attacken("Energieschuss", 6, 0, 0.8, "schaden", "%s hält seinen DingDong in die Luft und lässt einen kleinen Ball von leuchtender Energie auf den Gegner fliegen." %spieler.name)
lebensentzug = Attacken("Lebensentzug", 5, 0, 0.7, "lebensraub", "%s richtet seinen DingDong auf den Gegner und fängt an irgendeinen Mist zu murmeln. Plötzlich wird Lebensenergie vom Gegner auf %s übertragen" % (spieler.name, spieler.name))


#Klassen und Attackenzuweisung für den Spieler
spieler = Mage(spieler.name, {1: energieschuss, 2: lebensentzug})


fight(spieler, schwein)

















