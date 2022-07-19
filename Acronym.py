def generate_acronym():
    input_phrase = input(f'Enter an input phrase to generate Acronym \n')
    acronym = ''
    for s in input_phrase.split(' '):
        acronym += s[0]
    print(f'You acronym for {input_phrase} is : ', acronym.upper())

generate_acronym()