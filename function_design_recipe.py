def area(base, height):
    return base * height / 2


def perimeter(side1, side2, side3):

    ''' (number, number, number) -> number

    Return the perimeter of a traiange with the sides of the lenght
    side1, side2, side3

    >>> perimeter(3, 4, 5)
    12
    >>> perimeter(10.5, 6, 9.3)
    25.8
    '''
    return side1 + side2 + side3

def convert_to_celsius(fahrenheit):

    '''(number) -> float 
    Return the number of celsius degress equivalent to fahrenheit degresss.
    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    '''
    return (fahrenheit - 32) * 5 / 9
