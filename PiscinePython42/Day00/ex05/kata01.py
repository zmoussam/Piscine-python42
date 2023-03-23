kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

#for key in kata.keys():
 #   print(key, "was created by", kata[key])

for language, creator in kata.items():
    print(f"{language} was created by {creator}")