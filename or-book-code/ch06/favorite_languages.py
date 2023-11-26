favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jim': 'java',
    'tom': 'c++',
    'jerry': 'c',
    'mike': 'c++',
    'andrew': 'javascript',
    'carl': 'go',
    'james': 'javascript',
    'jane': 'javascript',
    'eric': 'rust',
    'john': 'rust',
    'joe': 'go',
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# Looping through all key-value pairs
# The items() method returns a list of key-value pairs
# The for loop then assigns each of these pairs to the two variables provided
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
# Using the keys() method with set and sorted functions
# The keys() method returns a list of keys
# The set() function removes duplicates
# The sorted() function sorts the keys alphabetically
print("\nLanguages:")
for language in sorted(set(favorite_languages.values())):
    print(language.title())