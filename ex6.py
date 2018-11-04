# coding=utf-8


x= "There are %d types of people . " %10

binary= 'binary'

do_not = "don't"

y = "Those who knows %s and those who %s ." %(binary , do_not)

print(x)

print(y)

print("I said : %r ." %x)

print("I also said : '%s' ." %y)

hilarious = False

joke_evaluation = "Isn't that joke so fun ?! %r ."

print(joke_evaluation%hilarious) #为什么不需要‘，’  #你想多了，括号里才需要‘，’

w = "This is the left side of ...."

e = "A string with right side. "

print(w+e)

