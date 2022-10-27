#This program was inspired by the code challenges as seen on freeCodeCamp.org. 

#Its main purpose is to help beginner programmers gain more hands on experience with developing programs in Python. 

#This main program is dependent on two additional scripts: help.py and ParameterGlossary.py.

#Along with its imported dependencies, PyChallengeCreator.py will generate up to 8 random data types and functions to be included in a program.

#Users can select their assigned parameters from a numbered list in order to get more information on their usage and syntax.

#Until formatting can be properly demonstrated in the syntax examples, users will be the most successful if they are already familiar with 
#the use of indentation and white space in Python programs. 
#See https://www.geeksforgeeks.org/indentation-in-python/ for more information. 

#This is a work in progress and any helpful suggestions for improving run time and string formatting are welcome!





def code_challenge_generator():
    import random, help
    
    
    string_methods = ['slice', 'len()', 'split()']
    rand_string_meth = random.choice(string_methods)
    
    string_methods2 = ['variable.capitalize()', 'variable.title()', 'variable.upper()', 'variable.lower()', 'variable.swapcase()', 'variable.replace()']
    rand_string_meth2 = random.choice(string_methods2)
    
    number_methods = ['addition +', 'subtraction -', 'multiplication *', 'floating point division /', 'integer (truncating) division', 'modulus %', 'exponetiation **']
    rand_numb_meth = random.choice(number_methods)
    
    big_tuple = 'a tuple that contains at least 3 lists'
    big_list = 'a list that contains at least three lists'
    big_dict = 'a dictionary of lists'
    large_data_type = ['list','dictionary', 'tuple', 'set', big_tuple, big_list, big_dict]
    rand_data = random.choice(large_data_type)
    
    if_list = ['variable.append() or +=', 'variable.insert(index, "new data")','del variable[index]', 'remove.variable()', 'variable.pop()', 'variable.copy()', 'variable = [expression for item in iterable]'] 
    rand_list = random.choice(if_list)
    
    if_tuple = ['tuple unpacking']
    
    if_dict = ['dict(dictionary)- create from additonal two item tuple or list', 'dictionary.update(addtional dictionary here)', 'del dictionary[value]', 'dictionary.clear()',\
              '"key" in dictionary', 'list( dictionary.keys() )', 'list( dictionary.values() )', 'list( dictionary.items() )', 'for value in variable.values()', 'for value in variable.items()'\
              '{key_expression: value_expression for expression in iterable}']
    rand_dict = random.choice(if_dict)
    if_set = ['variable = set()', 'set("string")', 'if "string" in set:', 'if value & {"string1", "string2"}:', 'value1 & value2 or value1.intersection(value2)',\
              'value1 | value2 or value1.union(value2)', 'value1 - value2 or value1.difference(value2)', 'value1 ^ value2 or value1.symmetric_difference(value2)',\
               'value1 <= value2 or value1.issubset(value2)', 'value1 >= value2 or value1.issuperset(value2)', 'variable = {expression for expression in iterable}'] 
    rand_set = random.choice(if_set)
    iterator_methods = ['while', 'conditional with break', 'if elif and else', 'for loop', 'for loop with continue', 'for items 1, 2, 3, 4 in zip(group1 group2 etc):']
    rand_iterator = random.choice(iterator_methods)
    generate_num = ['range(begin num, end num, by this increment)']
    function_params = ['arguments as needed', 'use of positional arguments (*args)', 'use of (**kwargs)'] 
    rand_params = random.choice(function_params)
    regular_rand_params = [rand_string_meth, rand_string_meth2, rand_numb_meth, rand_iterator, generate_num, rand_params]
    name = input("Enter your name:")
    
    print("Hello", name.strip(' '),", you have been tasked with coding a short Python program.")
     
    if rand_data == 'list' or big_list:
        print("Your program must contain each of the following:")
        print(rand_data)
        print(rand_list) 
        print(regular_rand_params)
    elif rand_data == 'dictionary' or big_dict:
        print("Your program must contain each of the following:")
        print(rand_data) 
        print(rand_dict)
        print(regular_rand_params)
    else:
        print("Your program must contain each of the following:")
        print(rand_data)
        print(rand_set) 
        print(if_tuple)
        print(regular_rand_params)

    answer = input("Do you need help? Type 'y' for help or 'q' to quit")
    if answer == 'y':
        help.helper_program()
    else:
        print('Good luck with your project!')
code_challenge_generator()



    