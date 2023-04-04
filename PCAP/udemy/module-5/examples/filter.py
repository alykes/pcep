print(list(filter(lambda i: i % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))) # The lambda specifies that each element should satisfy the condition


email_adresses = [
    'bob$gmail.com',
    'ango@gmail.com',
    'ans323gmail.com',
    'someone@hotmail.com',
    '4572389yahoo',
    '82390-a@yahoo.co.uk'
]

list(filter(lambda x : '@' in x, email_adresses))

