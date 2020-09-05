## Python

> some basic commands

> exit REPL cmd D

### basics

    'this is a string'
    "this is a string"
    'this is not"
    "first" "second"
    >>> "firstsecond"
    
    """this is 
       a multiline string
    >>> this is \na multiline string

    a = c
    print(a)

    1 + 7
    >>>8

    path = r'C:\path'

    type(a)
    >>> <type 'string'>

> \n is a new line,
> \' escaping a quote
> r'' is a raw string

### while

    C = 5
    while C != 0:
        print(c)
        c -=1

> ^c terminates loops

### if

    if "eggs":
     print("true")
    elif "bacon":
     print("smoked")
    else:
     print("false")

> elif is python for else if, obviously

### lists

    [1, 9, 8]

    a = ["apple", "pear", "lemon"]
    a(3);

    a.append("melon")
    list("characters")

#### dict

    d = {'alice':'878-8728-922'}

> maps keys to values (assoc array)
> might not be stored in the same order, entered.

#### for loop

    cities = ["London","New York","Pittsburgh","Barcelona"]
    for city in cities:
     print(city)


## setting up default python on mac os

Below command shows how it should be done:

    ln -s -f /usr/local/bin/python3.7 /usr/local/bin/python

Close the current terminal session or keep it that way and instead open a new terminal window (not tab). Run this:

    python --version
