tennis_ranking = {
    1: 'Ashleigh Barty',
    2: 'Naomi Osaka',
    3: 'Simona Halep'
}

for key in tennis_ranking.keys():
    print('key:', key, '\ttennis_ranking[key]:', tennis_ranking[key], '\ttennis_ranking[key][0]:', tennis_ranking[key][0])
    tennis_ranking[key] = tennis_ranking[key][0]    # This updates the dictionary value with the first letter of the value referenced by key
    print('New value of tennis_ranking[key]:', tennis_ranking[key])

print(tennis_ranking)       # {1: 'A', 2: 'N', 3: 'S'}
print(tennis_ranking[1]*2)  # AA