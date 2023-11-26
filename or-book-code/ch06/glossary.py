glossary = {
    'loop': 'a loop is a sequence of instructions that is continually repeated until a certain condition is reached.',
    'list': 'a list is a collection of items in a particular order.',
    'dictionary': 'a dictionary is a collection of key-value pairs.',
    'tuple': 'a tuple is a collection which is ordered and unchangeable.',
    'set': 'a set is a collection which is unordered and unindexed.',
    'if': 'an if statement consists of a boolean expression followed by one or more statements.',
    'elif': 'an elif statement is used to include multiple conditions.',
    'else': 'an else statement is used to include a default condition.',
    'for': 'a for loop is used for iterating over a sequence.',
    'while': 'a while loop is used to repeat a block of code multiple times.',
}

for term, definition in glossary.items():
    print(f"\n{term.title()}: {definition}")