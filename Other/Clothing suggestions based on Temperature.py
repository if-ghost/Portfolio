# Lab 9
# Temperature-based apparel recommendations

current_temperature = int(input('Hey there, I\'m your virtual image consultant. I\'m going to help you look presentable, no matter the weather conditions. May I ask the current temperature? '))

if 0 < current_temperature <= 15:
    print('It\'s a little chilly out there. I recommend a sweater and some jeans!')
elif 15 < current_temperature <= 35:
    print('It\'s a little on the warmer side right now. I recommend a T-shirt. Just avoid graphic tees! ')
elif 35 <= current_temperature:
    print('Wow! I\'m dying to know where you\'re located right now! I recommend you go bare, otherwise you might die of heatstroke!')
elif current_temperature < 0:
    print('Welcome to Canada. It\'s a typical day (unless you\'re in B.C.). Just get yourself a winter jacket and a hat. I would advise against a russian bomber hat though, not everyone can pull it off. A toque will do' )
elif current_temperature == 0:
    print('Water freezes at this temperature. But you\'re not water, so wear whatever feels comfortable')
else:
    print('It seems like we need to work on our communication skills, don\'t you think? ')