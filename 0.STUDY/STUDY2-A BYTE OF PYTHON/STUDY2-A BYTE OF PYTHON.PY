# 출처 [http://swaroopch.com/notes/python, A Byte of Python]


''' # [리스트 축약]
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo) '''


''' # [lamda식]
points = [ { 'x' : 2, 'y' : 3 },
 { 'x' : 4, 'y' : 1 } ]
points.sort(key=lambda i : i['y'])
print(points) '''


''' # [문자열]
# This is a string object
name = 'Swaroop'
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:
    print('Yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist)) '''



''' # [참조]
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist is just another name pointing to the same object!
mylist = shoplist
# I purchased the first item, so I remove it from the list
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that both shoplist and mylist both print
# the same list without the 'apple' confirming that
# they point to the same object
print('Copy by making a full slice')
# Make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# Notice that now the two lists are different '''


''' # [딕셔너리]
# 'ab' is short for 'a'ddress'b'ook
ab = { 'Swaroop' : 'swaroop@swaroopch.com',
 'Larry' : 'larry@wall.org',
 'Matsumoto' : 'matz@ruby-lang.org',
 'Spammer' : 'spammer@hotmail.com'
 }
print("Swaroop's address is", ab['Swaroop'])
# Deleting a key-value pair
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))
# Adding a key-value pair
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido']) '''


''' # [튜플]
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', \
 len(new_zoo)-1+len(new_zoo[2])) '''


''' # [리스트]
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:')
for item in shoplist:
    print(item,)
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist) '''


''' # [dir()함수]
a=10
b=20
c=print()
print(dir())
print(help(__annotations__)) '''


''' # [모듈의 name속성]
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module') '''


''' # [모듈]
import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n') '''


''' # [DocString]
def print_max(x, y):
    # Prints the maximum of two numbers.
    # The two values must be integers.
    # convert to integers, if possible
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
print_max(3, 5)
print(print_max.__doc__)
help(print_max) '''


''' # [return문]
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
print(maximum(2, 3)) '''


''' # [VarArgs 매개변수]
def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
        print(count)
        print(type(count))
    for key in keywords:
        count += keywords[key]
        print(count)
        print(type(count))
    return count
print(total(10, 1, 2, 3, vegetables=50, fruits=100)) '''


''' # [키워드 인수]
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100) '''



''' # [기본 인수값]
def say(message, times=1):
    print(message * times)
say('Hello')
say('World', 5) '''


''' #[global문]
x = 50
def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)
func()
print('Value of x is', x) '''


''' # [지역변수]
x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func(x)
print('x is still', x) '''


''' # [함수]
def say_hello():
    # block belonging to the function
    print('hello world')
# End of function
say_hello() # call the function
say_hello() # call the function again
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
# directly pass literal values
print_max(3, 4)
x = 5
y = 7
# pass variables as arguments
print_max(x, y) '''


''' # [continue문]
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 4:
        print('Too small')
        continue
print('Input is of sufficient length')
# Do other kinds of processing here... '''


''' # [braek문]
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
print('Length of the string is', len(s))
print('Done') '''


''' # [for문]
for i in range(1, 5):
     print(i)
else:
    print('The for loop is over') '''


''' # [while문]
number = 23
running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # Do anything else you want to do here
print('Done') '''


''' # [if문]
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here
print('Done')
# This last statement is always executed,
# after the if statement is executed. '''


''' # [수식 예제]
length = 5
breadth = 2
area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth)) '''


''' # [문자열 포매팅]
age=20
name='Swaroop'
print('{0} was {1} years old when eh wrote this book'.format(name,age))
print('Why is {0} playing with that python?'.format(name))
print('{} was {} years old when eh wrote this book'.format(name,age))
print('Why is {} playing with that python?'.format(name))
print('{0:.3f}'.format(1.0/3))
print('{0:_^11}'.format('hello'))
print('{name}wrote{book}'.format(name='Swaroop',book='A Byte of Python'))
print('a',end=" ")
print('b')
print(r"Your's man")
print('abcd\
e') '''