
import json
from difflib import get_close_matches 

data = json.load(open("data.json"))

def checkWord():
    word = input("Enter the word to search: ")
    close = get_close_matches(word, data.keys(), cutoff = 0.7)[0]
    word = word.lower()

    if word in data:
        return ' '.join(data[word])

    elif word.title() in data:
        return ' '.join(data[word.title()])

    elif word.upper() in data:
        return ' '.join(data[word.upper()])

    elif close in data:
        ans = input(f"Did you mean {close}? (Y or N)? ")
        ans = ans.lower()
        if ans == 'y':
            return ' '.join(data[close])
        elif ans == 'n':
            return "Seems like there is an issue, please try entering another word."
        else:
            return "Please enter y or n"

    else:
        return "Seems like there is an issue, please try entering another word."


print(checkWord())