def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def count_characters(text):
    characters_dict = {}
    for character in text:
        lowercase_character = character.lower()
        if lowercase_character in characters_dict:
            characters_dict[lowercase_character] += 1
        else:
            characters_dict[lowercase_character] = 1
    return characters_dict

def sort_on(items):
    return items["num"]

def sort_dictionary(dict):
    list_dict = []
    for key in dict:
        new_dict = {}
        new_dict["name"] = key
        new_dict["num"] = dict[key]
        list_dict.append(new_dict)
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

