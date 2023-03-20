sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

response = input('Enter a word in English or EXIT: ')

while response != 'EXIT':
    if response in sample_dict:
        print('Translation:', sample_dict[response])
    else:
        print('No match!')
        
    response = input('Enter a word in English or EXIT: ')

print('Bye!')


## provided solution ##
while True:
    user_input = input('Enter a word in English or EXIT: ')
    if user_input == 'EXIT':
        break
    if user_input in sample_dict:
        print ('Translation:', sample_dict[user_input])
    else:
        print('No match!')
 
print('Bye!')
