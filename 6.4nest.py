#6.4
#嵌套：可以将一系列字典存储在列表中，或将一系列列表存储在字典中

#列表中嵌套字典
aliens = []
alien_colors = ['green','yellow','red']
alien_points = [5,10,15]
alien_speeds = ['slow','medium','fast']
for alien_no in range(0,30):
    select = alien_no % 3
    alien_color = alien_colors[select]
    alien_point = alien_points[select]
    alien_speed = alien_speeds[select]
    new_alien = {'color':alien_color, 'point':alien_point, 'speed':alien_speed}
    aliens.append(new_alien)
for alien in aliens:
    print(alien)

#字典中嵌套列表
favorate_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python','haskell'],
}
for name,languages in favorate_languages.items():
    if len(languages) >= 2:
        print(name +"'s favorate languages are:")
    else:
        print(name+"'s favorate language is:")
    for language in languages:
        print('\t'+language.title())

#字典中嵌套字典
users ={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcruie':{
        'first':'marie',
        'last':'cruie',
        'location':'paris',
    },
}
for users_name,users_info in users.items():
    print("\nUser name:"+users_name)
    fullname = users_info['first']+' '+users_info['last']
    location = users_info['location']
    print("\tFull name:"+fullname)
    print("\tLocation:"+location)