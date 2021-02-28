# Press the green button in the gutter to run the script.
import random

# кидает монетку
def somefunc():
    return random.choice(['орёл', 'решка'])

# выполняет что-то несколько раз и говорит, сколько раз получился ожидаемый исход
def doSomethingMultipleTimes(times, func, predicate):
    result = 0
    for i in range(times):
        if (predicate(func())):
            result += 1
    return result

if __name__ == '__main__':
    count = doSomethingMultipleTimes(3000, somefunc, lambda x: x == 'орёл')
    print(count)