#string = input("Please enter a word:") 
#string = [n for n in input('Enter numbers: ').split()]
#def palin(word1):

def palindrome(word):
    word = input("Please enter a word:") 
    word = word.lower().replace(' ', '')
    if not word.isalpha():
      return '{} is not a string. Enter srings only'.format(word) 
    if list(word) == list(reversed(word)):
        return "{} is a palidrome".format(word)
    return "{} is not a palidrome".format(word)

      
print(palindrome(word))

word = input("Please enter a word:") 
word = word.lower().replace(' ', '')
if not word.isalpha():
    print '{} is not a string. Enter srings only'.format(word) 
if list(word) == list(reversed(word)):
    print "{} is a palidrome".format(word)
print "{} is not a palidrome".format(word)

      
#print(palindrome(word))