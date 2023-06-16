split_string = 'This string is split here\n and then its split here \n and I am going to split it here \n'
print(split_string)
tabbed_string = 'Tab here \t and tab here \t and here \t,'
print(tabbed_string)
splitting_string_with_newline = '''This string is split via a backslash
and then its split here
and then again here
haha'''
unsplitting_string_with_backslash = '''This string is split via a backslash \\ and then its split here \\ and then again here \\ haha'''
print(splitting_string_with_newline)
print(unsplitting_string_with_backslash)
# esacping backslashes in a string with a backslash
print('\\usr\\bin\\local\\tim')
# esacping balckshaes with a raw string
print(r'\usr\bin\local\tim')