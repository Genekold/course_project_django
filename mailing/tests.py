def divade(x, y):
    if y == 0:
        raise ValueError('Not')
    return x / y



if __name__ == '__main__':
    x = int(input('x = '))
    y = int(input('y = '))
    try:
        print(divade(x, y))
    except ValueError as e:
        print(e)