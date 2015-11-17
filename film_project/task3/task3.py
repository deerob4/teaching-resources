import sqlite3 as lite


def run_query(query):
    con = lite.connect('films.db')

    with con:
        cur = con.cursor()
        cur.execute(query)

        return cur.fetchall()


def input_films(quantity):
    for x in range (quantity):
        print('\nFilm #{0}:'.format(x + 1))
        print('--------')

        run_query('INSERT INTO films (title, genre, director, rating) VALUES ("{0}", "{1}", "{2}", "{3}")'.format(
            input('What is the film called? '),
            input('What genre does the film belong to? '),
            input('Who directed the film? '),
            int(input('How would you rate the film out of 10? '))
        ))

    find_films('alphabetical')


def find_films(method):
    if method == '1':
        display_films(run_query('SELECT * FROM films ORDER BY title ASC'))

    elif method == '2':
        display_films(run_query('SELECT * FROM films ORDER BY rating'))

    elif method == '3':
        genre = input('Which genre do you want to view? ')
        display_films(run_query('SELECT * FROM films WHERE genre = "{0}"'.format(genre)))

    elif method == '4':
        average = run_query('SELECT AVG(rating) FROM films')

        print('The average rating of all your films is {0}'.format(average[0][0]))
        
    elif method == '5':
        genres = run_query('SELECT DISTINCT genre FROM films')
        values = []
        for genre in genres:
            values.append({
                "genre": genre,
                "rating": run_query('SELECT MAX(rating) FROM films WHERE genre = "{0}"'.format(genre))
            })
            
        for value in values:
            print('Highest rating in {0} category is {1}'.format(value['genre'], value['rating']))


def display_films(films):
    print('\nYour films:\n')

    for film in films:
        print('Title:', film[1])
        print('Genre:', film[2])
        print('Director:', film[3])
        print('Rating:', str(film[4]) + '\n')


if __name__ == '__main__':
    while True:
        task = input('Do you want to add films(1) or view them(2)? ')
        if task == '1':
            quantity = int(input('\nHow many films do you want to enter? '))
            input_films(quantity)
        elif task == '2':
            method = input('\nHow do you want to view the films? There are five ways:\n1. Alphabetically\n2. By highest rating\n3. By genre\n4. Average rating\n5. Highest rating in each genre')
            find_films(method)
