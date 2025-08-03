frank_path = "./books/frankenstein.txt"

def get_num_words(path_to_file):
    with open(path_to_file) as f:
        num_words = 0
        file_contents = f.read()
        for f in file_contents.split():
            num_words += 1
        return num_words

def get_characters(path_to_file):
    my_dict = {}
    with open(path_to_file) as input_string:
        for char in input_string.read():
            if char.isalpha():
                character = char.lower()
                if character in my_dict:
                    my_dict[character] += 1
                else:
                    my_dict[character] = 1
        return my_dict

def sort_on(items:dict):
    return items["num"]

def create_character_list(input: dict):
    dict_list = []
    for i in input:
        if i.isalpha():
            x = {"char": i, "num": input[i]}
            dict_list.append(x)
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list
