def get_longest_word(sample_story):
    rep_story = sample_story.replace(',', ' ')
    rep_story = rep_story.replace('.', ' ')
    rep_story = rep_story.split()
    # can be replaced by word_list = sample_story.replace(',', ' ').replace('.', ' ').split()

    longest_word = ''

    for element in rep_story:
        if len(element) > len(longest_word):
            longest_word = element
    
    return (longest_word)


sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''

get_longest_word(sample_story)


######### Suggested solution
# def get_longest_word(input_string):
#     words = input_string.replace('.', ' ').replace(',', ' ').split()
#     temp_max_word = ''
 
#     for word in words:
#       if len(word) > len(temp_max_word):
#         temp_max_word = word
    
#     return temp_max_word