#this function out puts the text in print once called.

def helloworld():  #here we are defining this function helloworld()
    print("This is the output once the function is called.") #here is what will be executed once the function is called.
#A function will not execute itself unless it is called.

helloworld() # here we are calling this function to get it executed.

#as we have len() function to determine length of a string.
#print(len('helloworld')) it is one example however it is commented out.

# we will name a function called length to determine the length.

def length():# here length function is defined
    print(len('My name is Prakalpit'))#it will determine the length of the text 'My name is Prakalpit'.
    print(len('Determine length'))  # here it will determine the length of 'Determine length'.

length() # the function is called here.

# in below function we will call the function 3 times as for to print the text 3 times
def multiprint():
    print("this will be printed multiples of time")

#now we will call this function.
multiprint()#this all program wqill output the same result
multiprint()
multiprint()
