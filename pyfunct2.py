#we will define a function named hellopy()

def hellopy(parameters):# the variable stored here is called parameters.
    print("hello: " + parameters +". How are you?")
#when we call the function, between the parenthesis we will add what we want to be printed in the sentence.
hellopy('Argument')#the thing we add between the parenthesis is called arguement.

def myshow(name):# here the parameter is name

#line 8 the def statement defines the function myshow()

    print(name + ' welcome to my show.')
#the calling of the function passes the string value 'Prakalpit'(which is an argument.) to the parameter.
myshow("Prakalpit")#the arguement is Prakalpit
#line12 now calls the function to be executed

#we will now create a global variable name spam with the value 21.
spam=21 # spam is a global variable.
#we now will define a function named compare as we are writing this program to compare global and local variable.
def compare(local): #parameter local is the local variable.
    print(local + ' Hello. How are you doing these days.', ' Oh yes! are you ' + str(spam) + ' years old.')
    # in line 21 local is a local variable and spam is a global variable meaning spam can be used both within and out
    # of the function whereas local can not. for example using print(local) out of the function compare() will give
    # name error.

compare('parakalpit')
