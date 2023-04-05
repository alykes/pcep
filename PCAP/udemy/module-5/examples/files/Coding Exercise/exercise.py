def count_occurences(file_name, word):
    
    found = 0
    
    try:
        stream = open(file_name)

        for line in stream:
            word_list = line.replace(',', '').replace('.', '').split()
            print(word_list)

            for i in word_list:
                if (i.lower() == word.lower()):
                    found += 1
        
    except Exception as e:
        print('An error occured:', e)

    finally:
        stream.close()

    return (found)


f_name_one = 'first_text_file.txt'
f_name_two = 'second_text_file.txt'

print(count_occurences(f_name_one, 'the'))
print(count_occurences(f_name_two, 'the'))
