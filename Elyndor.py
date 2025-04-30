import random
import os
import time

# === MONSTERS ===
monsters = [
    {"name": "Shadow Bat", "hp": 25, "dmg": (5, 10)},
    {"name": "Slime Crawler", "hp": 20, "dmg": (3, 8)},
    {"name": "Bone Wraith", "hp": 35, "dmg": (6, 12)},
    {"name": "Frost Spider", "hp": 22, "dmg": (4, 9)},
    {"name": "Dark Imp", "hp": 18, "dmg": (2, 7)},
    {"name": "Moss Troll", "hp": 40, "dmg": (4, 11)},
    {"name": "Fire Wasp", "hp": 15, "dmg": (7, 14)},
    {"name": "Cave Golem", "hp": 50, "dmg": (3, 8)},
    {"name": "Thunder Snake", "hp": 30, "dmg": (5, 12)},
    {"name": "Void Rat", "hp": 12, "dmg": (4, 6)},
    {"name": "Stone Gremlin", "hp": 27, "dmg": (4, 10)},
    {"name": "Whispering Ghost", "hp": 20, "dmg": (6, 9)},
    {"name": "Ash Walker", "hp": 34, "dmg": (7, 13)},
    {"name": "Swamp Maw", "hp": 28, "dmg": (4, 11)},
    {"name": "Crimson Viper", "hp": 21, "dmg": (6, 14)},
    {"name": "Rock Crusher", "hp": 55, "dmg": (5, 10)},
    {"name": "Iron Wolf", "hp": 33, "dmg": (7, 12)},
    {"name": "Toxic Beetle", "hp": 19, "dmg": (4, 8)},
    {"name": "Night Owl", "hp": 17, "dmg": (3, 7)},
    {"name": "Blazing Moth", "hp": 23, "dmg": (5, 9)},
    {"name": "Spirit Echo", "hp": 25, "dmg": (6, 10)},
    {"name": "Hollow Beast", "hp": 48, "dmg": (6, 12)},
    {"name": "Venom Lurker", "hp": 29, "dmg": (4, 9)},
    {"name": "Fanged Root", "hp": 36, "dmg": (5, 10)},
    {"name": "Silent Shade", "hp": 26, "dmg": (3, 8)},
    {"name": "Phantom Bat", "hp": 18, "dmg": (4, 9)},
    {"name": "Dune Scorpion", "hp": 32, "dmg": (6, 11)},
    {"name": "Moon Bear", "hp": 42, "dmg": (7, 13)},
    {"name": "Glacier Claw", "hp": 38, "dmg": (5, 10)},
    {"name": "Netherling", "hp": 24, "dmg": (4, 9)},
    {"name": "Obsidian Ant", "hp": 20, "dmg": (5, 10)},
    {"name": "Lava Hopper", "hp": 22, "dmg": (6, 11)},
    {"name": "Spineback Toad", "hp": 30, "dmg": (4, 8)},
    {"name": "Cursed Hare", "hp": 15, "dmg": (7, 12)},
    {"name": "Twilight Fox", "hp": 28, "dmg": (5, 10)},
    {"name": "Rustfang", "hp": 34, "dmg": (6, 12)},
    {"name": "Plague Mite", "hp": 19, "dmg": (5, 9)},
    {"name": "Marrow Worm", "hp": 23, "dmg": (3, 7)},
    {"name": "Crystal Raven", "hp": 31, "dmg": (6, 11)},
    {"name": "Howling Thorn", "hp": 40, "dmg": (5, 13)}
]

# === GAME VARIABLES ===
player_hp = 100
player_weapon = {"name": "Wooden Sword", "dmg": (5, 10)}
inventory = [player_weapon]
kill_count = 0
in_battle = False
current_monster = None

# === SPECIAL SMILEY SWORD ===
if os.path.exists("id.smyid"):
    smiley_sword = {"name": "Smiley Sword", "dmg": (15, 25)}
    inventory.append(smiley_sword)
    player_weapon = smiley_sword

# === SEED ===
seed = input("Enter a world seed: ")
random.seed(seed)

# === MONSTER PICK FUNCTION ===
def spawn_monster():
    if seed.lower() == "elder":
        return dict(monsters[30])  # Obsidian Ant
    else:
        return dict(random.choice(monsters))

# === GAME LOOP ===
print("\nWelcome to Elyndor Battle Beta 1.1!\n")
while True:
    time.sleep(1)
    if not in_battle and random.randint(1, 8) == 1:
        current_monster = spawn_monster()
        in_battle = True
        print(f"A wild {current_monster['name']} appeared! HP: {current_monster['hp']}")

    if in_battle:
        print("\n[1] Attack  [2] Heal (+20 HP)  [3] Run  [4] Switch Weapon")
        action = input("Your choice: ")

        if action == "1":
            dmg = random.randint(*player_weapon["dmg"])
            current_monster["hp"] -= dmg
            print(f"You hit the {current_monster['name']} for {dmg} damage.")

            if current_monster["hp"] <= 0:
                print(f"You defeated the {current_monster['name']}!")
                kill_count += 1
                player_hp += 5
                player_weapon["dmg"] = (player_weapon["dmg"][0]+1, player_weapon["dmg"][1]+1)
                in_battle = False
            else:
                mdmg = random.randint(*current_monster["dmg"])
                player_hp -= mdmg
                print(f"The {current_monster['name']} hits you for {mdmg} damage.")

        elif action == "2":
            player_hp += 20
            print("You healed +20 HP.")

        elif action == "3":
            print("You ran away!")
            in_battle = False

        elif action == "4":
            print("Available weapons:")
            for i, w in enumerate(inventory):
                print(f"{i+1}: {w['name']} (Damage: {w['dmg'][0]} - {w['dmg'][1]})")
            choice = int(input("Choose weapon number: ")) - 1
            if 0 <= choice < len(inventory):
                player_weapon = inventory[choice]
                print(f"Equipped {player_weapon['name']}.")

    print(f"HP: {player_hp} | Kills: {kill_count}")
    
    if player_hp <= 0:
        print("\nYou have fallen in battle. Game Over.")
        break