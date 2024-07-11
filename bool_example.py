def is_even(num):
    ''' (number) -> bool

    Return whether num is even
    
    >>> is_even(4)
    True
    >>> is_even(77)
    False
    '''
    return  num %2 == 0
##
##    if num %2 == 0:
##        return True
##    else:
##        return False
##    

def is_comfortable(temp):
    '''(number) -> bool

    Return whether temp is 22.5.
    >>> is_comfortable(22.5)
    True
    >>> is_comfortable(20)
    False
    '''

##    if temp == 22.5:
##        return True
##    else:
##        return False

    return temp == 22.5
##
##    if temp == 22.5:
##        return True
##    elif temp != 22.5:
##        return False

def fruit_color(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'
