message = "Hello Python World!"
print(message)

#2.1 Simple Message
simple_message = "This is a further message"
print(simple_message)

#2.2 Re-assign a message variable
further_message = "Another message... but different"
print(further_message)
further_message = "Reassigned further message"
print(further_message)

#2.3 Personal Message
personal_name = "Dave"
personal_message = f"Hello {personal_name}, would you like to learn some python today?"
print(personal_message)

#2.4 Name cases
name_case_changer = "James Smith"
print(name_case_changer.lower())
print(name_case_changer.upper())
print(name_case_changer.title())

#2.5 Famous Quote
einstein_quote = 'Einstein once said "Common sense is merely the collection '\
'of prejudices we\'ve attained by the age of 18"'
print(einstein_quote)

#2.6 Famous Quote 2
famous_person = "albert einstein"
famous_quote = f'{famous_person.title()} once said "Common sense is merely the collection '\
'of prejudices we\'ve attained by the age of 18"'
print(famous_quote)

#2.7 Stripping names
person_name = "    Reggie Miller     "
print(person_name)
print(person_name.strip())
print(person_name.lstrip())
print(person_name.rstrip())

#2.8 file_extension
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

#2.9 number 8 (simple operations)
print(5+3)
print(4*2)
print(16/2)
print(9-1)

#2.10 favourite number
favourite_number = 7
my_favourite_number = f"My favourite number is {favourite_number}"
print(my_favourite_number)

