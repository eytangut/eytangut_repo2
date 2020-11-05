from classes.game import Person , bcolors
magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)
running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    print("=============================================")
    player.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. ENEMY HP:" ,enemy.get_hp(), )
    if 
    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("enemy attacked for", enemy_dmg, "player HP:", player.get_hp())
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "you win" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "your enemy has defeted you!" + bcolors.ENDC)
        running = False
