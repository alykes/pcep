# Tuples in lists

city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Athens', 'Greece', 3.1)

capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Athens', 'Greece', 3.1)]

for capital in capitals:
    print('Capital:', capital[0], ' Country:', capital[1], ' Population (mil):', capital[2] )


# Lists in Tuples
user_data = ('Chad', 'American', 1969, [78.0, 78.2, 77.5]) # This is a list inside a tuple
user_data[3].append(79.6) # You can append to the list inside the tuple!


##### CODING EXERCISE #####
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
    
counter = 0
total_time = 0

for flights in connections:
    if flights[1] == 'Rome':
        counter += 1
        total_time += flights[2]

average_time = total_time / counter
print(counter, 'connections lead to Rome with an average flight time of',average_time ,'minutes')