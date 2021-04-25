# to create SHA-1 hashes
import hashlib
# for open and read the wordlist file from URL
from urllib.request import urlopen


def readWordList(url):
    try:
        wordListFile = urlopen(url).read()
    except Exception as e:
        print("fk u there is an exception while reading the file")
        exit()

    return wordListFile


def hash(password):
    """the hashlib.sha1 function expects the argument to be of type <class 'bytes'>
    which is why we are passing password.encode() as its argument."""
    result = hashlib.sha1(password.encode())
    # return a hexadecimal digits
    return result.hexdigest()


def bruteForce(guessPasswordList, actualPasswordHash):
    wordFound = False
    # loop over the whole password list
    for guessPassword in guessPasswordList:
        """if the guessed password after being hashed is equal to the actual
        hashed password then we got the real password"""
        if (hash(guessPassword) == actualPasswordHash):
            print("the password is:", guessPassword)
            wordFound=True
            return wordFound
    return wordFound


# the password file (I didn't make this file)
url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'

# the password you are searching in a file
actualPassword = "hello"
actualPasswordHashed = hash(actualPassword)
# wordlist variable stores the wordlist as a UTF-8 string
# removing decode('UTF-8') the file will be read like this
# '123456\npassword\n123456789\n12345678\n12345\........
wordList = readWordList(url).decode('UTF-8')

# each password in the wordlist is separated by a "\n" character.
# So we split this wordlist into a List and store it in guesspasswordlist variable.
guessPasswordList = wordList.split('\n')
print(wordList)
wordFound=bruteForce(guessPasswordList, actualPasswordHashed)
totalNoWords = 0
# counting the number of words in the given URL
for noWords in wordList:
    totalNoWords += 1

print("number of words in the url is: ", totalNoWords)
if wordFound!=True:
    print("I couldn't guess this password ")
