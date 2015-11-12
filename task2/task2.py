import sqlite3 as lite

con = lite.connect('films.db')


def input_films(quantity):
    for x in range (quantity):
        print('\nFilm #{0}:'.format(x + 1))
        print('--------')

        save_film({
            'title': input('What is the film called? '),
            'genre': input('What genre does the film belong to? '),
            'director': input('Who directed the film? '),
            'rating': int(input('How would you rate the film out of 10? '))
        })

    display_films()


def save_film(film):
    with con:
        cur = con.cursor()

        cur.execute('INSERT INTO films (title, genre, director, rating) VALUES ("{0}", "{1}", "{2}", "{3}")'.format(
            film['title'],
            film['genre'],
            film['director'],
            film['rating']
        ))


def display_films():
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM films')
        films = cur.fetchall()

        print('\nYour films:\n')

        for film in films:
            print('Title:', film[1])
            print('Genre:', film[2])
            print('Director:', film[3])
            print('Rating:', str(film[4]) + '\n')


if __name__ == '__main__':
    quantity = int(input('How many films do you want to enter? '))
    input_films(quantity)