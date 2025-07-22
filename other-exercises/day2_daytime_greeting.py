# write a function that greets you with the time of day
# it takes an optional parameter: moment, which is otherwise right now

from datetime import datetime, time


def greet(moment=None):
    if moment is None:
        moment = datetime.now().time()

    morning = time(12, 0)
    noon = time(17, 0)
    evening = time(21, 0)

    if moment < morning:
        return 'good morning!'
    elif morning <= moment < noon: 
        return 'good afternoon'
    elif noon <= moment < evening:
        return 'good evening'
    else:
        return 'good night'

    
print(greet())
print(greet(time(18, 0)))
