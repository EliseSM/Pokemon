# ------------------------------------------------------
#        Name: Elise Schatzki-McClain
#    Filename: hmwk9.pdf
#     Section: L02
#        Date: 4/11/2019
#  References: https://bulbapedia.bulbagarden.net/wiki/Type, https://pokemondb.net/pokedex/national
# ------------------------------------------------------

import random

#this creates a basic pokemon character
class Pokemon():

    #this initializes all the characteristics of the pokemon
    def __init__(self, name, pokemon_type, max_hp, attack_power, defensive_power):
        self.name = name
        self.pokemon_type = pokemon_type
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack_power = attack_power
        self.defensive_power = defensive_power
        self.fainted = "FALSE"
        self.lives = 2
        self.type = "---"
        
    #this prints out all the the current characteristics of the pokemon
    def printStats(self):
        print("My name is", self.name)
        print("I am a", self.pokemon_type)
        print("My max hit points is:", self.max_hp)
        print("My current hit points is:", self.current_hp)
        print("My attack power is:", self.attack_power)
        print("My defensive power is:", self.defensive_power)
        print("My fainting state:", self.fainted)
        print("I have", self.lives, "lives")

    #this the reaction of the pokemon if it is attacked
    def defend(self):
        hurt = self.defensive_power - 2 #this is how much the pokemon is hurt in hitpoints
        self.current_hp = self.current_hp - hurt
        if self.current_hp < 1:
            self.fainted = "TRUE"

    #this the reaction if the pokemon is attacked by a weaker pokemon
    def half_defend(self):
        hurt = self.defensive_power - 2 
        half_hurt = hurt / 2  #this is half the normal amount of hurt
        self.current_hp = self.current_hp - hurt
        if self.current_hp < 1:
            self.fainted = "TRUE"

    #this is the attack hurting the other players hit points
    def attack(self, opponent):
        opponent.defend()

    #this revives the pokemon to half the max hitpoints
    def revive(self):
        if self.lives > 0:
            #there are only two possible revivings
            if self.fainted == "TRUE":
                self.current_hp = self.max_hp / 2
                self.fainted = "FALSE"
                self.lives = self.lives - 1
                return(True)
            else:
                
                return(False)
        #this is what happens when the poke has run out of lives
        print("You don't have any lives left! You're DEAD!")
        
    #This is a replenishing mechanism that gives 2 hitpoints to all pokes regardless of type
    def waterbreak(self):
        self.current_hp = self.current_hp + 2
    #this is a method of hit points that hurts all pokes equally, no matter the type
    #this is the reaction of being punched by another opponent
    def punched(self):
        print("Ooof!")
        self.current_hp = self.current_hp - 3

#This is the method that prompts the player to take a turn
def take_turn(player1, player2):
    print("Player, take your turn!!! Good luck!")
    #here they are given options depnding on what action they want to take
    the_play = input("REVIVE, WATERBREAK, PUNCH, or ATTACK ")
    #here the action is performed
    if the_play == "REVIVE" or the_play == "revive":
        player1.revive()
    elif the_play == "ATTACK" or the_play == "attack":
        player1.attack(player2)
    elif the_play == "WATERBREAK" or the_play == "waterbreak":
        player1.waterbreak()
    elif the_play == "PUNCH" or the_play == "punch":
        player2.punched()
    #if the player does not choose from the actions, they forfit their turn
    else:
        print("Huh? Player forfits turn...")



#This is a function that allows pokes to battle eachother
def battle(Pokemon1, Pokemon2):
    print("========================")
    print("AND THE BATTLE BEGINS...")
    print("========================")

    #here it prints the players stats to start the battle
    print("Player1:")
    Pokemon1.printStats()
    print("Player2:")
    Pokemon2.printStats()

    
    fate = "no"
    #this loops through rounds of turns until a player has been claimed winner
    while fate == "no" or fate == "NO":
        #this calls to the take turn function for each player
        print(" ")
        print("========================")
        print("Pokemon1 turn:")
        take_turn(Pokemon1, Pokemon2)

        print(" ")
        print("========================")
        print("Pokemon2 turn:")
        take_turn(Pokemon2, Pokemon1)

        #this then prints the players stats fter the set of turns
        print(" ")
        print("========================")
        print(" ")
        print("Player1:")
        Pokemon1.printStats()

        print(" ")
        print("Player1:")
        Pokemon2.printStats()
        print(" ")
        #this breaks the loop if someone has won
        fate = input("Has anyone won yet? (yes or no)")
        
    #this congratulates the winner
    winner = input("Who won the battle?")
    print("Congrats " + winner + "! YOU WON!  ;)   ;)   ;)   ;)")


#this introduces the subclass Mew with psychic powers
class Mew(Pokemon):
  def __init__(self,name, pokemon_type, max_hp, attack_power, defensive_power):
      super().__init__(name, pokemon_type, max_hp, attack_power, defensive_power)
      self.type = "PSYCHIC"
  
  def attack(self, opponent):
      if (opponent.type == "FIGHT" or opponent.type == "POISON"):
        # super-effective
        # do twice as much damage
        opponent.defend()
        opponent.defend()
        
      elif (opponent.type == "PSYCHIC" or opponent.type == "STEEL"):
        # not effective
        # do half as much damage
        opponent.half_defend()

      else:
        opponent.defend()

        
#this introduces the subclass Sylveon with fairy powers
class Sylveon(Pokemon):
  def __init__(self,name, pokemon_type, max_hp, attack_power, defensive_power):
      super().__init__(name, pokemon_type, max_hp, attack_power, defensive_power)
      self.type = "FAIRY"
    
  
  
  def attack(self,opponent):
      if (opponent.type == "DARK" or opponent.type == "DRAGON" or opponent.type == "FIGHT"):
          #super-effective
          #do twice as much damage
          opponent.defend()
          opponent.defend()
        
        
      elif (opponent.type == "FIRE" or opponent.type == "POISON" or opponent.type == "STEEL"):
          #not effective
          #do half as much damage
          opponent.half_defend()

      else:
          opponent.defend()
        
        
#this introduces the subclass Darkrai with dark powers
class Darkrai(Pokemon):
  def __init__(self,name, pokemon_type, max_hp, attack_power, defensive_power):
      super().__init__(name, pokemon_type, max_hp, attack_power, defensive_power)
      self.type = "DARK"
  
  def attack(self, opponent):
      if (opponent.type == "ICE" or opponent.type == "ROCK"):
        # super-effective
        # do twice as much damage
        opponent.defend()
        opponent.defend()

        
      elif (opponent.type == "ELECTRIC" or opponent.type == "FIRE" or opponent.type == "STEEL" or opponent.type == "WATER"):
        # not effective
        # do half as much damage
        opponent.half_defend()

      else:
        opponent.defend()

#this introduces the subclass Kyogre with water powers
class Kyogre(Pokemon):
  def __init__(self,name, pokemon_type, max_hp, attack_power, defensive_power):
      super().__init__(name, pokemon_type, max_hp, attack_power, defensive_power)
      self.type = "WATER"
  
  def attack(self, opponent):
      if (opponent.type == "FIRE" or opponent.type == "GROUND" or opponent.type == "ROCK"):
        # super-effective
        # do twice as much damage
        opponent.defend()
        opponent.defend()
        
      elif (opponent.type == "DRAGON" or opponent.type == "GRASS" or opponent.type == "WATER"):
        # not effective
        # do half as much damage
        opponent.half_defend()

      else:
        opponent.defend()

#this forces the player to create a pokemone character
def player_creation(name):
    #this randomizes the power of their pokemon
    hp = random.randint(15, 25)
    ap = random.randint(3, 14)
    dp = random.randint(3, 14)

    #this allows the user to choose which type of pokemon they want to play
    poke_type = input("What type of Pokemon do you want to be? (Mew, Sylveon, Darkrai, Kyogre, Anonymous)")
    
    poke = Pokemon(name, poke_type, hp, ap, dp)

    #This creates the pokemon character using the variables created above
    if poke_type == "Mew":
        print("Congrats, you are PSYCHIC!")
        final_pokemon = Mew(name, poke_type, hp, ap, dp)
        return(final_pokemon)
    elif poke_type == "Sylveon":
        print("Congrats, you are FAIRY!")
        final_pokemon = Sylveon(name, poke_type, hp, ap, dp)
        return(final_pokemon)
    elif poke_type == "Darkrai":
        print("Congrats, you are DARK!")
        final_pokemon = Darkrai(name, poke_type, hp, ap, dp)
        return(final_pokemon)
    elif poke_type == "Kyogre":
        print("Congrats, you are WATER!")
        final_pokemon = Kyogre(name, poke_type, hp, ap, dp)
        return(final_pokemon)
    else:
        return(poke)

    
#This controls the game/guides through the game
def main():
    #welcoming message
    print("|||||||||||||||||||")
    print("WELCOME TO POKEMON!")
    print("|||||||||||||||||||")

    #allows players to choose names and sends them to finish creating pokemons
    name_1 = input("Player 1, Choose a name: ")
    poke_1 = player_creation(name_1)

    print(" ")
    name_2 = input("Player 2, Choose a name: ")
    poke_2 = player_creation(name_2)
    
    #this prints the pokemon stats before the battle starts
    print(" ")
    poke_1.printStats()
    print(" ")
    poke_2.printStats()

    #this initiates the battle mode
    battle(poke_1, poke_2)
    
    


main()
