def calc(n1, n2, oper):
    assert isinstance(n1, (int, float)), 'N1 precisa ser int ou float'
    assert isinstance(n2, (int, float)), 'N2 precisa ser int ou float'
    
    match(oper):
        case '-':
            return n1 - n2
        case '+':
            return n1 + n2 
        case '/':
            return n1 / n2
        case '*':
            return n1 * n2
        
try:
    print(calc(3, '4', '*'))
except AssertionError as e:
    print(str(e))

print(calc(5, 7, '/'))