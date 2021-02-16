# # by Kami Bigdely
# # Extract class
# first_names = ['elizabeth', 'Jim']
# last_names = ['debicki', 'Carrey']
# birth_year = [1990, 1962]
# movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
#      ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
# emails = ['deb@makeschool.com', 'jim@makeschool.com']
#
# def send_hiring_email(email):
#     print("email sent to: ", email)
#
# for i, value in enumerate(emails):
#     if birth_year[i] > 1985:
#         print(first_names[i], last_names[i])
#         print('Movies Played: ', end='')
#         for m in movies[i]:
#             print(m, end=', ')
#         print()
#         send_hiring_email(value)

class Actor:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def send_hiring_email(self):
        print("email sent to: ", self.email)

actor1 = Actor('elizabeth', 'debicki', 1990, ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'], 'deb@makeschool.com')
actor2 = Actor('Jim', 'Carrey', 1962, ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man'], 'jim@makeschool.com')

actors = [actor1, actor2]

for actor in actors:
    if actor.birth_year > 1985:
        print(actor.first_name, actor.last_name)
        print('Movies Played: ', end='')
        for m in actor.movies:
            print(m, end=', ')
        print()
        actor.send_hiring_email()
