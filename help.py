import ParameterGlossary
def helper_program():

#runs only if you need help, input prompt given at the end of main program 
#prints a numbered list of parameters
#asks for user input (a number from the list)
#returns defintion of parameter and syntax usage
#asks if you still need help 
#loop continues until user no longer needs help ( user input does not equal 'Y') 



    print("Parameter List")
    print("String Methods: \n1. slice \n2. len() \n3. split()")
    print("Number Methods: \n4. floating point division \n5. integer truncating division \n6. modulus % \n7. exponentiation **")
    print("Data Types: \n8. list \n9. dictionary \n10. tuple \n11.set")
    print("List Methods: \n12. variable.append() or += \n13. variable.insert(index, 'new data','new data') \n14. del variable[index] \n15. remove.variable() \n16. variable.pop() \n17. variable.copy() \n18. variable = [expression for item in iterable]")
  
    print("Tuple Method: \n19. tuple unpacking")

    print("Dictionary Methods: \n20 . dict(dictionary)- create from additonal two item tuple or list \n21. dictionary.update(addtional dictionary here) \n22. del dictionary[value] \n23. dictionary.clear() \
              \n24. 'key' in dictionary \n25.list( dictionary.keys() )\n26. list( dictionary.values() ) \n27. list( dictionary.items() ) \n28. for value in variable.values() \n29. for value in variable.items() \
              \n30. {key_expression: value_expression for expression in iterable}")

    print("Set Methods: \n31. variable = set() \n32. set('string') \n33. if 'string' in set: \n34. if value & {'string1', 'string2'}: \n35. value1 & value2 or value1.intersection(value2) \
              \n36. value1 | value2 or value1.union(value2) \n37. value1 - value2 or value1.difference(value2) \n38. value1 ^ value2 or value1.symmetric_difference(value2) \
               \n39. value1 <= value2 or value1.issubset(value2) \n40. value1 >= value2 or value1.issuperset(value2) \n41. variable = {expression for expression in iterable}") 

    print("Iterator Methods: \n42. while \n43. conditional with break \n44. if, elif and else \n45. for loop \n46. for loop with continue \n47. for items 1, 2, 3, 4 in zip(group1 group2 etc)") 

    print("Generator Method: \n48. range(begin num, end num, by this increment)")
    print("Argument Parameters: \n49. use of positional arguments (*args) \n50. use of (**kwargs)")

    
    ParameterGlossary.parm_glossary()




