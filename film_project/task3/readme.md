Task 3 - Querying the Database
==============================
Now extend your program so that it returns the films in a certain manner, based on the selected query. You should implement the following queries:

* Films in alphabetical order by title, descending (A - Z)
* All films in a certain genre
* Films in order of rating (descending)
* The average (mean) of all ratings
* The highest ranking in each genre

You should display a list of these options at the start of the program, and allow the user to choose which one they want. There should still be the option to add films. The program should follow this general flow:

    Do you want to add films(1) or view them(2)? 2

    How do you want to view the films? There are 4 ways:
    1. Alphabetical order
    2. Films in a certain genre
    3. Films in order of rating
    4. Average of all ratings
    5. Higest scoring film in each genre

    2

    Which genre do you want to view? heist

    Your heist films:

    Title: The Italian Job
    Genre: heist
    Director: Peter Collinson
    Rating: 9

    Title: Heat
    Genre: heist
    Director: Michael Mann
    Rating: 7

    4

    The average rating of all your films is 8.
