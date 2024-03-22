def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        count_words = len(file_contents.split())
        print(count_words)

def count_chars():
    with open("books/frankenstein.txt") as f:
        read_contents = f.read()
        #words = len(file_contents.split())
        lowered_string = read_contents.lower()
        character_dict = dict()


        for character in lowered_string:
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
            
    return character_dict

if __name__ == "__main__":
    main()



