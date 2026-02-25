# # # # # alien_0={
# # # # #     'color':'green',
# # # # #     'points':5
# # # # # }

# # # # # print(alien_0['color'])

# # # # # new_points=alien_0['points']

# # # # # print(f"you just earned {new_points} points!")

# # # # # alien_0['x_position']=0
# # # # # alien_0['y_position']=25

# # # # # print(alien_0)





# # # # # # x ="""hhhhhhhhhhhhhhhhhhhhhhhhhh
# # # # # #       ksksssss"""

# # # # # # print(x)

# # # # alien_0 ={}

# # # # alien_0['color']='green'

# # # # # alien_0['points']=5

# # # # # print(alien_0)

# # # # # del alien_0['points']

# # # # print(alien_0)

# # # # alien_0['points']=20

# # # # point_value=alien_0.get('points','No point value assigned')

# # # # # print(point_value)


# # # # user_0={
# # # #     'uname':'efermi',
# # # #     'first':'enrico',
# # # #     'last':'fermi',
# # # # }

# # # # for key,value in user_0.items():
# # # #     print(f"\nKey:{key}")
# # # #     print(f"Value:{value}")


# # favorite_languages = {
# #     'jen': 'python',
# #     'sarah': 'c',
# #     'edward': 'ruby',
# #     'phil': 'python',
# # }

# # # 1. Standard loop for existing users
# # for name in favorite_languages.keys():
# #     print(f"Hi {name.title()}.")
# #     if name in ['phil', 'sarah']:
# #         language = favorite_languages[name].title()
# #         print(f"\t{name.title()}, I see you love {language}!")

# # # 2. Check for missing users OUTSIDE the loop
# # if 'erin' not in favorite_languages:
# #     print("\nErin, please take our poll!")


# alien_0={
#     'color':'green',
#     'points':5
# }

# alien_1={
#     'color':'yellow',
#     'points':10
# }


# alien_2={
#     'color':'red',
#     'points':15
# }

# aliens =[alien_0,alien_1,alien_2]

# for alien in aliens:
#     print(alien)


from calendar import c


aliens = []

for alien_number in range(30):
    new_alien ={
        'color':'green',
        'points':5,
        'speed':'slow'
    }

    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
    print("...")

print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'

for alien in aliens[:5]:
    print(alien)
    print("...")