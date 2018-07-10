#Default Arguments 2

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
		It could be called like this:

#cheeseshop("Limburger", "It's very runny, sir.",
#           "It's really very, VERY runny, sir.",
#           shopkeeper="Michael Palin",
#           client="John Cleese",
#           sketch="Cheese Shop Sketch")
#and of course it would print:

#-- Do you have any Limburger ?
#-- I'm sorry, we're all out of Limburger
#It's very runny, sir.
#It's really very, VERY runny, sir.
#----------------------------------------
#shopkeeper : Michael Palin
#client : John Cleese
#sketch : Cheese Shop Sketch
#Note that the order in which the keyword arguments are printed is guaranteed to match the order in which they were provided in the function call.

# When a final formal parameter of the form **name is present, it receives a dictionary containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name)