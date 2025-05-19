def pig_latin(sentence):
    # Write your solution here!
    words = sentence.split()
    new_words_list = []
    for word in words:
        new_word = alter_one_word(word)
        new_words_list.append(new_word)
    return " ".join(new_words_list)

def alter_one_word(word):
    if word[0] in ["a", "e", "i", "o", "u"]:
        return word
    new_word = word[1:] + word[0] + "ay"
    return new_word

# TC: O(1) + O(1) = O(1) --> O(n) = O(n)
# SC: O(1) + O(n) = O(n)

# Test cases

assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")