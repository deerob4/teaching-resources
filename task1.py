def input_films(quantity):
    films = []

    for x in range (quantity):
        print('\nFilm #{0}:'.format(x + 1))
        print('--------')

        films.append({
            'title': input('What is the film called? '),
            'category': input('What category does the film belong to? '),
            'director': input('Who directed the film? '),
            'rating': int(input('How would you rate the film out of 10? '))
        })

    display_films(films)


def display_films(films):
    print('\n\nHere are your films:\n')

    for film in films:
        for prop in film:
            print('{0}: {1}'.format(prop.title(), film[prop]))


if __name__ == '__main__':
    quantity = int(input('How many films do you want to enter? '))
    input_films(quantity)