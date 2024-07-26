import doctest

def sum(n1, n2):
    """ sum n1 e n2

    >>> sum(10, 20)
    30

    """    
    return n1 + n2 
        
doctest.testmod(verbose=True)
print(sum(5, 7))