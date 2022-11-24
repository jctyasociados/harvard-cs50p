def main():
    """ Python script that converts emoticons to smily emoji and to frowny emoji """
    str_to_convert = input("Input string containing smiley or frowney emoticons: \n").strip()
    print(convert(str_to_convert))


def convert(str_to_convert):
    """ Function that converts emoticons into emojis """
    converted_str = str_to_convert.replace(":(", "🙁").replace(":)", "🙂")
    return converted_str
    
main()
