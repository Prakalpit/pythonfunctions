# here we will just global and local variable to a greater extent.
spam=input('Enter your name: ')
# we created input with in the variable spam
spam1=input("What do you want to watch: Bike racing, Horse racing or car racing?: ")#here we created next variable
def myShow(name):# we defined function myShow().
    print(name + ' Welcome to my show.', end=' ')
    print('So, you want to watch ' + spam1 + '.')#here we using the second variable within the function.

myShow(spam) # here we are using whatever the input() will store in the first variable spam as an argument.

