def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        count_words = len(file_contents.split())
        print("--- Begin report of books/frankenstein.txt ---") 
        print(str(count_words) + " " + "words found in the document")

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
                
    mini_dict_list = []

    for character,count in character_dict.items():
            mini_dict =  {"char": character, "count": count}
            
            mini_dict_list.append(mini_dict)
    
    sorted_mini_lists = sorted(mini_dict_list, key =lambda x: x["count"], reverse=True)
    
    for item in sorted_mini_lists:
        print(f"The '{item['char']}' character was found {item['count']} times")
    
    print("--- End report ---")


  
    #return character_dict

if __name__ == "__main__":
    main()
    count_chars()



