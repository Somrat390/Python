# #                  scope 

# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()

# print(f"enemies outside function: {enemies}")

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

# # Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#         drink_potion()

# drink_potion()

# print(player_health)


# # ################ There is no block scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)



############## Modify Global Scope

# enemies = 1

# def increase_enemies():
#     # global enemies
#     # enemies += 1
#     print(f"enemies inside function: {enemies}")
#     return enemies+1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# ######################## Global constant

PI = 3.14159
URL = "https://hello.com"
