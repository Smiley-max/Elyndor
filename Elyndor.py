import random
import time
import os

# === SWORD DEFINITIONS ===
default_swords = [
    {"name": "Rusty Sword", "level": 1, "bonus": 2},
    {"name": "Iron Blade", "level": 2, "bonus": 3},
    {"name": "Silver Saber", "level": 3, "bonus": 4},
    {"name": "Golden Edge", "level": 4, "bonus": 6},
    {"name": "Crystal Sword", "level": 5, "bonus": 8}
]

# Check for smiley sword
has_smiley_sword = os.path.exists("id.smyid")
if has_smiley_sword:
    default_swords.append({"name": "Smiley Sword", "level": 6, "bonus": 10})
    print("Smiley Sword unlocked! You feel a joyful power inside you...")

# Start with Rusty Sword
current_sword = default_swords[0]
inventory = [current_sword]

# === MONSTERDATA ===
monster_list = [
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

# === GAME INIT ===
seed = input("Enter your Elyndor seed: ")
random.seed(seed)

hp = 100
max_hp = 100
monsters_defeated = 0
in_battle = False

print("\nWelcome to Elyndor!")
print(f"You wield the {current_sword['name']} (Level {current_sword['level']}).")
print("Type 'attack', 'heal', 'leave' during battle.")
print("Type 'switch' outside battle to change your sword.\n")

# === GAME LOOP ===
while True:
    time.sleep(1)

    if not in_battle and random.randint(1, 8) == 1:
        monster = random.choice(monster_list)
        monster_name = monster["name"]
        monster_hp = monster["hp"]
        monster_dmg_range = monster["dmg"]

        in_battle = True
        print(f"\nA wild {monster_name} appears! It has {monster_hp} HP!")

        while monster_hp > 0:
            action = input("Your action (attack/heal/leave): ").lower()

            if action == "attack":
                damage = random.randint(5, 10) + current_sword["bonus"]
                monster_hp -= damage
                print(f"You strike with your {current_sword['name']} for {damage} damage! {monster_name} has {max(monster_hp, 0)} HP left.")
                
                if monster_hp > 0:
                    monster_attack = random.randint(*monster_dmg_range)
                    hp -= monster_attack
                    print(f"The {monster_name} hits you for {monster_attack}! You have {max(hp, 0)} HP left.")
                    if hp <= 0:
                        print("You have fallen in battle. Game Over.")
                        exit()
                else:
                    print(f"You defeated the {monster_name}!")
                    monsters_defeated += 1
                    hp = min(max_hp, hp + 10)
                    print(f"You gain 10 HP. Current HP: {hp}")

                    if monsters_defeated % 3 == 0:
                        new_sword = random.choice(default_swords)
                        if new_sword not in inventory:
                            inventory.append(new_sword)
                            print(f"You found a new sword: {new_sword['name']} (Level {new_sword['level']})!")

                    in_battle = False

            elif action == "heal":
                print("You can't heal during battle!")

            elif action == "leave":
                print(f"You run away from the {monster_name}.")
                in_battle = False
                break

            else:
                print("Unknown command.")

    elif not in_battle:
        action = input("Action outside battle (wait/switch/heal/status): ").lower()

        if action == "wait":
            continue
        elif action == "heal":
            hp = min(max_hp, hp + 15)
            print(f"You rest and heal. HP: {hp}")
        elif action == "status":
            print(f"HP: {hp}/{max_hp} | Sword: {current_sword['name']} (Level {current_sword['level']})")
        elif action == "switch":
            print("Your swords:")
            for i, sword in enumerate(inventory):
                print(f"{i+1}: {sword['name']} (Level {sword['level']})")

            choice = input("Choose sword number: ")
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(inventory):
                    current_sword = inventory[idx]
                    print(f"You equip the {current_sword['name']}!")
                else:
                    print("Invalid sword number.")
            else:
                print("Please enter a valid number.")
