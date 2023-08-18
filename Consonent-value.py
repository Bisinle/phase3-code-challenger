# import re
# no_vowels = re.sub("[aieou]", ",", string)


def consonent_value(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_postion = {char: index for index, char in enumerate(alphabet)}
    vowels = [("a", ","), ("e", ","), ("o", ","), ("i", ","), ("u", ",")]

    string = "".join(
        string.replace(char, vowel) for char, vowel in vowels if char in string
    )
    grouped = [char for char in string.split(",") if char.isalpha()]
    grouped_list = list()
    for g in grouped:
        grouped_added = 0
        if len(g) > 1:
            for i in g:
                grouped_added += alpha_postion.get(i) + 1
            grouped_list.append(grouped_added)
        else:
            grouped_added += alpha_postion.get(g) + 1
            grouped_list.append(grouped_added)

    return max(grouped_list)


print(consonent_value("strength"))
