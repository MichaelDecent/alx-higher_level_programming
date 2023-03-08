#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        for n in range(1, i):
            if (i == (n * 15)):
                print('FizzBuzz', end=' ')
                break
            elif (i == (n * 3)):
                print('Fizz', end=' ')
                break
            elif (i == (n * 5)):
                print('Buzz', end=' ')
                break
        else:
            print(i, end=' ')
