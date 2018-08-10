

def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return start


@coroutine
def grep(pattern):
    print(f'Looking for {pattern}')
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('Gone away... Goodbye.')


if __name__ == '__main__':
    g = grep('python')

    g.send('Yeah but no')
    g.send('bla')
    g.send('python is awsome')
    g.close()
