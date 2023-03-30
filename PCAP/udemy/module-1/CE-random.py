import math
import random

def generate_tickets(ticket_count, max_number):
    
    number_list = []
        
    unique_numbers = [i for i in range(0, max_number)]
    number_list = random.sample(unique_numbers, ticket_count)
    winning_number = random.choice(number_list)
    
    return(number_list, winning_number)


print(generate_tickets(5, 10))
print(generate_tickets(8, 50))


#### Suggested solution
# import random
# 
# def generate_tickets(ticket_count, max_number):
#     list_to_return = random.sample(range(0, max_number), ticket_count)
#     return (list_to_return, random.sample(list_to_return, 1)[0])