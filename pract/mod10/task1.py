import re
import doctest

def is_correct_password(password):
    """
    Function for checking password

    >>> is_correct_password('rtG3FG!Tr^e')
    True
    >>> is_correct_password('aA1!*!1Aa')
    True
    >>> is_correct_password('oF^a1D@y5e6')
    True
    >>> is_correct_password('enroi#$rkdeR#$092uWedchf34tguv394h')
    True
    >>> is_correct_password('пароль')
    False
    >>> is_correct_password('password')
    False
    >>> is_correct_password('qwerty')
    False
    >>> is_correct_password('lOngPa$$$W0Rd')
    False

    """
    pattern = r'(\d+[a-z]+[A-Z]{2,}[^$%@#&*!?]{2,}.{6,}(.)\1\1'
    if re.fullmatch(pattern, password):
        return True
    else:
        return False


doctest.testmod()
