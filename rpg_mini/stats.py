import random
 
class Player:
    def __init__(self, name):
        """Initialize the player with a name, inventory, health, and stats."""
        self.name = name
        self.inventory = []
        self.health = 100
        self.strength = 10
        self.intelligence = 10
        self.speed = 10
        self.level = 1
        self.experience = 0
 
    def level_up(self):
        """Level up the player and allocate points to stats."""
        self.level += 1
        self.strength += 5
        self.intelligence += 5
        self.speed += 5
        print(f"{self.name} has leveled up to level {self.level}!")
        print("Allocate points to strength, intelligence, and speed.")
 
    def show_stats(self):
        """Display the player's current stats."""
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Speed: {self.speed}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")
 
rooms = {
    'Hall': {
        'description': "You are in a grand hall with several doors leading in different directions.",
        'items': {'key': "A small rusty key.", 'map': "A map showing the layout of the dungeon."},
        'exits': {'north': 'Kitchen', 'east': 'Combat Room', 'south': 'Library', 'west': 'Pantry'}
    },
    'Kitchen': {
        'description': "You are in a kitchen with a lingering smell of old food. There are pots and pans scattered around.",
        'items': {'knife': "A sharp kitchen knife.", 'apple': "A fresh, red apple."},
        'exits': {'south': 'Hall', 'east': 'Trapdoor Room'}
    },
    'Trapdoor Room': {
        'description': "You fell through a trapdoor! You can't go back the way you came.",
        'items': {},
        'exits': {'west': 'Kitchen'}
    },
    'Combat Room': {
        'description': "A dark room where a monster awaits you. Prepare for battle!",
        'items': {},
        'exits': {'west': 'Hall', 'east': 'Treasure Room'}
    },
    'Pantry': {
        'description': "You are in a small pantry filled with shelves of food and supplies.",
        'items': {'bread': "A loaf of bread.", 'cheese': "A piece of cheese."},
        'exits': {'east': 'Hall'}
    },
    'Treasure Room': {
        'description': "A small room glittering with treasure!",
        'items': {'gold': "A pile of gold coins.", 'jewel': "A sparkling jewel."},
        'exits': {'west': 'Combat Room'}
    },
    'Library': {
        'description': "You are in a dusty library filled with ancient books.",
        'items': {'spellbook': "An old spellbook with mysterious symbols."},
        'exits': {'north': 'Hall', 'east': 'Study'}
    },
    'Study': {
        'description': "You are in a quiet study with a large desk and a flickering candle. Papers are scattered everywhere.",
        'items': {'letter': "A letter written in an unfamiliar language.", 'quill': "A feathered quill."},
        'exits': {'west': 'Library'}
    }
}
 
def describe_room(room):
    """Display the description, items, and exits in the current room."""
    print(f"\n{rooms[room]['description']}")
    if rooms[room]['items']:
        print("Items in the room:")
        for item, description in rooms[room]['items'].items():
            print(f"- {item}: {description}")
    else:
        print("There are no items in this room.")
 
    print("Exits:")
    for direction, next_room in rooms[room]['exits'].items():
        print(f"- {direction}: {next_room}")
    print()  # Add an extra newline for better readability
 
def describe_all_rooms():
    """Display descriptions and exits for all rooms."""
    for room_name, room_info in rooms.items():
        print(f"Room: {room_name}")
        print(f"Description: {room_info['description']}")
        if room_info['items']:
            print("Items in the room:")
            for item, description in room_info['items'].items():
                print(f"- {item}: {description}")
        else:
            print("There are no items in this room.")
        print("Exits:")
        for direction, next_room in room_info['exits'].items():
            print(f"- {direction}: {next_room}")
        print()  # Add extra newline between rooms for readability
 
def pick_up_item(player, room, item):
    """Allow the player to pick up an item and show its description."""
    if item in rooms[room]['items']:
        player.inventory.append(item)
        print(f"You picked up {item}.")
        print(rooms[room]['items'][item])
    else:
        print("Item not found in the room.")
 
def use_item(player, item):
    """Use an item from the player's inventory."""
    if item in player.inventory:
        if item == 'apple':
            player.health += 10
            player.inventory.remove(item)
            print("You eat the apple and regain 10 health.")
        elif item == 'knife':
            player.strength += 5
            print("You whip out your knife, increasing your strength by 5.")
        elif item == 'sword':
            player.strength += 10
            print("You're so strong with your big sword drawn!")
        elif item == 'bread':
            player.speed += 10
            print("You ate some carbs, increasing your speed by 10.")
        elif item == 'cheese':
            player.health -= 5
            print("You ate some cheese, but you're lactose intolerant, decreasing your health by 5.")
        elif item == 'spellbook':
            player.intelligence += 20
            player.strength -= 5
            print("You learned a new spell, increasing your intelligence by 20, but it took a lot of mental effort, decreasing your strength by 5.")
        elif item == 'gold':
            print("You feel the gold in your pocket and smile.")
        elif item == 'jewel':
            print("You feel the jewel in your pocket and say 'my precious', looking around, paranoid.")
        elif item == 'letter':
            player.strength += 5
            print("You read some gibberish on the letter, but it motivates you, increasing your strength by 5.")
        elif item == 'quill':
            print("Don't worry, every little thing quill be alright.")
        else:
            print(f"{item} can't be used right now.")
    else:
        print("You don't have that item in your inventory.")
 
def combat(player, monster):
    """Engage in combat between the player and a monster."""
    player_health = player.health
    monster_health = monster['health']
 
    while player_health > 0 and monster_health > 0:
        if 'sword' in player.inventory:
            player_attack = random.randint(10, player.strength + 10)
            print("You wield your sword and prepare for battle!")
        else:
            player_attack = random.randint(1, player.strength)
        monster_attack = random.randint(1, 20)
        monster_health -= player_attack
        player_health -= monster_attack
 
        print(f"You attack the monster for {player_attack} damage. Monster health: {monster_health}")
        print(f"The monster attacks you for {monster_attack} damage. Your health: {player_health}")
 
        if player_health <= 0:
            print("You have been defeated by the monster. You are D-E-D DED! Game Over.")
            break
 
    if player_health > 0:
        print("You have defeated the monster!")
        player.experience += 50
        if player.experience >= player.level * 100:
            player.level_up()
    else:
        player.health = 0  # Set health to 0 if the player dies
        print("You have been defeated by the monster. You are D-E-D DED! Game Over.")
 
def main():
    player = Player(name="Hero")
    current_room = 'Hall'
 
    print("Welcome to the RPG game!")
    print("Type 'look' to see the room description.")
    print("Type 'go <direction>' to move to a different room.")
    print("Type 'get <item>' to pick up an item.")
    print("Type 'use <item>' to use an item from your inventory.")
    print("Type 'stats' to see your stats.")
    print("Type 'map' to see an overview of all rooms.")
    print("Type 'quit' to exit the game.")
 
    while True:
        command = input("> ").strip().lower().split()
        if not command:
            continue
 
        action = command[0]
 
        if action == 'look':
            describe_room(current_room)
        elif action == 'map':
            describe_all_rooms()
        elif action == 'go':
            if len(command) < 2:
                print("Go where?")
                continue
            direction = command[1]
            if direction in rooms[current_room]['exits']:
                current_room = rooms[current_room]['exits'][direction]
                describe_room(current_room)
                if current_room == 'Combat Room':
                    combat(player, monster={'type': 'Goblin', 'health': 50})
            else:
                print("You can't go that way.")
        elif action == 'get':
            if len(command) < 2:
                print("Get what?")
                continue
            item = command[1]
            pick_up_item(player, current_room, item)
        elif action == 'use':
            if len(command) < 2:
                print("Use what?")
                continue 
            item = command[1]
            use_item(player, item)
        elif action == 'stats':
            player.show_stats()
        elif action == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid command.")
 
if __name__ == "__main__":
    main()