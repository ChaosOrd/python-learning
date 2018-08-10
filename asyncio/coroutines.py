def grep(pattern):
    print(f'Looking for {pattern}')
    while True:
        line = (yield)
        if pattern in line:
            print(line)


if __name__ == '__main__':
    g = grep('python')

    g.send(None)
    g.send('Yeah but no')
    g.send('bla')
    g.send('python is great')
