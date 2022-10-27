
def parm_glossary():
    
    query = int(input("Enter the number of the item you need help with:"))
    if query == 1:
        print('''Slice is a method for extracting a substring from a larger string. Syntax is: StringVariable[start:end:step]. [:] will
        extract the entire string. [start:] specifies where to start extracting. [:end] specifies from the beginning to the end offset minus 1.
        [::step] allows you to skip when extracting characters.[-3::] would specify collecting the last three characters from the end of a string.
        [18:-3] specifies starting at the 18th character of a string and stopping at the 4th character from the end. [::-1] and [-1::-1] will 
        reverse a string''')
       
    elif query == 2: 
        print("The len() function counts characters in a string. Syntax is: len(StringVariable)")
    elif query == 3: 
        print("The split() function is used to break a string into a list of smaller strings based on a separator character. Syntax is\
        : StringVariable.split('') where the character that you would like to separate the string by is listed between the quotation marks. For example:\
         confusing = 'Hirhowrareryour?' readable = confusing.split('r').")
    elif query == 4:
        print("Floating point division uses the / symbol and returns a decimal. For example 7 / 2 = 3.5")
    elif query == 5: 
        print("Integer (truncating) division uses the // symbol and returns the whole number of times a number is divisble by. For example 7 // 2 = 3")
    elif query == 6:
        print("Modulus returns the remainder or what is left over when dividing two numbers evenly. For example 7 % 3 = 1")
    elif query == 7:
        print("Exponentiation uses the ** symbols and finds a number to the specified power. For example 3 ** 4 = 81")

    elif query == 8: 
        print("Lists keep track of things in order and are mutable. You can specify that a data type is a list by using empty square brackets []. Using the\
        list() function also creates an empty list.")
    elif query == 9:  
        print("A dictionary is like a list that contains key/value pairs. Each key must be unique. They are mutable and are specified by curly brackets {}.") 
    elif query == 10: 
        print("A tuple is like a list but is immutable. Tuples are specified by using empty parantheses (). Tuples are helpful because they use less space\
        , can be used as dictionary keys and are passed as function arguments.") 
    elif query == 11:
        print("A set is like a dictionary with it's values thrown away leaving only keys. You use sets when you only want to know if something exists.\
        A null or empty set contains no like values. A union of two sets will have at least one key in common. The keys in common themselves is called an\
        intersection")
    elif query == 12: 
        print("The append() function allows you to add items onto the end of mutable data type. Syntax is: Variable.append('something new')")
    elif query == 13: 
        print("The insert() function allows you to input an item anywhere in a data type. Syntax is: Variable.insert(index#, 'something new')")
    elif query == 14:  
        print("del is a python statement, not a list method. Use it to delete an item by it's offset. Syntax is: del variable[index]")
    elif query == 15: 
        print("The remove() function allows you to delete something by its value. Syntax is: variable.remove('what_you_want_gone')")
    elif query == 16:
        print("The pop() function allows you to get and delete an item. The default value is the last item of the list but you can specify the index of what you\
        would like removed by placing the index number in the parantheses. Syntax is: variable.pop(index#)")
    elif query == 17:
        print("The copy() function allows you to copy the values of a list into a new one without affecting the original list you copied from. Syntax is:\
        newThing = original.copy()")
    elif query == 18: 
        print("The list comprehension [expression for item in iterable] is a more compact way to create a data structure from one or more iterators. For example:\
        number_list = [number for number in range(1,6)]. An additonal example with a conditonal: a_list = [number for number in range(1,6) if number % 2 == 1]")
    elif query == 19: 
        print("You can assign multiple variables at once with tuple unpacking. Syntax is: bunch_of_stuff = ('apple', 'orange', 'banana') a,b,c = bunch_of_stuff\
        a will equal apple, b will equal orange, etc.")
    elif query == 20: 
        print("The dict() function converts two-value sequences into a dictionary. The first item in a sequence is used as the key and the second as the value. Syntax is:\
        lot = [('a', 'b'), ('c', 'd'), ('e', 'f')] dict(lot) = {'c' :'d', 'a': 'b', 'e': 'f'}")
    elif query == 21:
        print("The update() function can be used to copy the keys and values of one dictionary into another. Syntax is: some_dict.update(another_dict). If the new dictionary\
        that is added also contains the key of the previous one, the second or newly added value of said key replaces the original value.")
    elif query == 22: 
        print("You can delete an item by it's key by using del dictionary_name['key_value']")
    elif query == 23:
        print("The clear() function deletes all key/value pairs from a dictionary. Syntax is: dict_name.clear(). You can also reassign the dictionary to an empty pair of\
       curly braces {}.")
    elif query == 24: 
        print("You can find out if a key exists in a dictionary by typing 'Key' in dictionary. Syntax is: 'Key name' in dictionary_name. You can also get an item by writing the dictonary name\
        followed by the key value in brackets.")
    elif query == 25: 
        print("You can use the keys() function to get all of the keys in a dictionary. Syntax is: list( dict_name.keys() )")
    elif query == 26: 
        print("You can use the values() function to get all of the values in a dictonary. Syntax is: list( dict_name.values() )")
    elif query == 27:
        print("You can get all of the key/value pairs from a dictionary by using the items() function. Syntax is: list( dict_name.items() )")
    elif query == 28:
        print("Use this to iterate over the values in a dictionary. Syntax is: for value in dict_name.values():")
    elif query == 29: 
        print("Use this to iterate over the key and value pairs in a dictionary. Syntax is: for key, value in dict_name.items(): or for item in\
        dict_names.items():")
    elif query == 30: 
        print("This dictionary comprehension allows you to create a data structure through one or more iterators. Syntax is: {key_expression : value_expression for expression\
        in iterable}. For example: letter_counts = {letter: word.count(letter) for letter in word}. This will count any repeated letters in a string. ")
    elif query == 31: 
        print("The set() function creates an empty set. You can also convert other data types into a set but any repeated values will be eliminated. Using set() to convert a dictionary\
        will only return the dictionary's keys. Syntax is: variable = set() or set('string')")
    elif query == 32 | 33: 
        print("To determine whether something exists in a set, you need to iterate it's values and apply a conditional. An example of this using a dictionary is:\
        for key, value in dict_name.items():\n    if 'value_string' in values:")
    elif query == 34: 
        print("You can use a combination operator to check for a combination of set values. The ampersand or '&' is the set intersection operator. It's syntax is:\n\
        for key, value in dict_name.items():\n    if value & {'content_combo1', 'content_combo2'}:")
    elif query == 35: 
        print("You can determine the intersection or the members that are common to two sets with with either syntax: set_name1 & set_name2 or set_name1.intersection(set_name2)")
    elif query == 36:  
        print("You can get the union or all of the members of either set by using the following syntax: set_name1 | set_name2 or set_name1.union(set_name2)")
    elif query == 37: 
        print("You can get the difference, or members of the first set but not the second by using the following syntax: set_name1 - set_name2 or set_name.difference(set_name2)")
    elif query == 38: 
        print("To find the items in one set or another but not in both, use either of the following syntax: set_name1 ^ set_name2 or set_name1.symmetric_difference(set_name2)")
    elif query == 39: 
        print("In order to check if one set is a subset of another (all members of the first set are also in the second set, use either of the following syntax:\
        \nset_name1 <= set_name2 or set_name1.issubset(set_name2). Will return a boolean value")
    elif query == 40:
        print("To determine if all of the members of the second set are also members of the first, use either of the following syntax: set_name1 >= set_name2 or\
        set_name1.issuperset(set_name2). Any set is a superset of itself.\nIn order to find a proper superset where the first set has all members of the second and more use either syntax:\
        set_name1 > set_name2. You cannot be a proper superset of yourself.")
            
    elif query == 41: 
        print("The syntax for a set comprehension is the following: {expression for expression in iterable}. For example:\n\
        a_set = {number for number in range(1,6) if number % == 1}")
    elif query == 42: 
        print("Use the 'while' looping mechanism to create functions under a specific condition. Example of its syntax: \n\
        count = 1\nwhile count<= 5:\n     print(count)\n    count += 1")
    elif query == 43:
        print('''You can use break if you have an infinite loop. Example of its syntax: \nwhile True: 
        \n    stuff = input('string to captialize [type q to quit]:')\n    if stuff == 'q':\n        break''')
    elif query == 44:
        print("If, elif and else statements apply at least three logical conditions in which to execute code. Syntax is as follows:\
        if value == condition1 :\n    print('its condition one!')\nelif value == condition2\n    print('its conditon two!')\nelse:\
        \n    print('its nothing, fugettaboutit!')")
    elif query == 45:
        print("A 'for' loop iterates through a data type to satisfy a condition for code execution. Syntax is as follows:\
        \nthings = ['cat', 'dog', 'bird']\nfor animal in things:\n    print(animal)")
    elif query == 46: 
        print("You can skip ahead through a loop with the 'continue' keyword. Syntax is as follows:\nfor number in range(1,6):\n\
        print(number)\nif number == 3:\n    continue")
    elif query == 47: 
        print("You can iterate over multiple sequences in parallel by using the zip() function. Syntax statement based off of gathering items from four separate lists is as follows\
        \n for thing1, thing2, thing3, thing4 in zip(group1, group2, group3, group4):")
    elif query == 48:
        print("You can generate a range of numbers with the range() function. Syntax is: range(start, stop, step) where indicating a value in the start place will initiate a number range from\
        that specific number(would be from 0 otherwise). The stop place will indicate the limit of the range and the step place indicates which values to increment/decrement by. A -1 value in the step place will move the range backwards")
    elif query == 49:
        print("When positioned as a parameter within a function, an asterisk groups a varied number of positional arguments into a tuple of paramter values. Example: \n\
        def print_this_and_that(thing1, thing2, *whatever):\n    print(thing1, thing2, whatever)\nprint_this_and_that('peanut butter', 'jelly', 'pringles', 'banana', 'Elvis')")
    elif query == 50:
        print("Use two asterisks ** to group keyword arguments (key and value pairs) into a dictionary. Syntax is as follows:\def print_kwargs(**kwargs):\n    print('Keyword arguments:', kwargs).\nCall this function with new key/value pairs as arguments.")
    else:
        print("Quit it! Only numbers 1-50 allowed!")
    
    
    
    more_help = input("Do you need help with anything else? Type Y for Yes or N for No (answer is case sensitive):")
    while more_help == 'Y':
        parm_glossary()
        more_help = ' '
        if more_help != 'Y':
            break
           
    


