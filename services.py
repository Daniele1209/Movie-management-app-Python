from Entities import Movie, Client, Rental
from errors import ServiceError
import datetime


class ServiceMovies(object):

    def __init__(self, repoMovies, validMovies,repoUndo):
        self.__repoMovies = repoMovies
        self.__validMovies = validMovies
        self.__repoMovies.generate_movies()
        self.__repoUndo = repoUndo

    def add_movie(self, m_id, m_title, m_desc, m_genre,availability, stats):
        movie = Movie(m_id, m_title, m_desc, m_genre,availability,stats)
        self.__validMovies.validate_movie(movie)
        self.__repoUndo.add_action(('add_movie', movie))
        self.__repoMovies.add(movie)

    def remove_movie(self, m_id):
        movie = self.__repoMovies.getMovie(m_id)
        self.__repoUndo.add_action(('remove_movie', movie))
        self.__repoMovies.remove(movie)

    def update_movie(self, m_id, title, description, genre, availability):
        movie = self.__repoMovies.getMovie(m_id)
        stats = movie.get_movie_stats()
        new_movie = Movie(m_id, title, description, genre, availability, stats)
        self.__repoUndo.add_action(('update_movie', movie, new_movie))
        self.__repoMovies.update_movie(movie, new_movie)

    def get_movies(self):
        return self.__repoMovies.get_all()

    def search_movie(self, option, string):
        if int(option) == 1:
            return self.__repoMovies.search_id(string)
        elif int(option) == 2:
            return self.__repoMovies.search_title(string)
        elif int(option) == 3:
            return self.__repoMovies.search_desc(string)
        elif int(option) == 4:
            return self.__repoMovies.search_genre(string)

    def show_rent_stats(self):
        return self.__repoMovies.movie_stats()

class ServiceRentals(object):

    def __init__(self,  repoRentals, validRentals, repoMovies, repoClients, repoUndo):
        self.__repoRentals = repoRentals
        self.__validRentals = validRentals()
        self.__repoMovies = repoMovies
        self.__repoClients = repoClients
        self.__repoRentals.generate_rentals()
        self.__repoUndo = repoUndo

    def get_rentals(self):
        return self.__repoRentals.get_all()

    def rent_movie(self, rental_id, movie_id, client_id, date, due_date):

        movie = self.__repoMovies.getMovie(movie_id)
        self.__repoMovies.check_movie(movie)
        client = self.__repoClients.getClient(client_id)
        self.__repoClients.check_client(client)

        self.__repoRentals.verify_valid(client_id, date)

        if movie.get_availability():
            movie.set_availability(False)
        else:
            raise ValueError("Movie is already being rented !")
        rental = Rental(rental_id,movie_id,client_id, date, due_date, None, 0)
        self.__validRentals.validate_rentals(rental)
        self.__repoRentals.add_rental(rental)

    def return_movie(self, rent_id, ret_date):
        valid = 1
        for rent in self.__repoRentals.get_rentals():
            if rent.get_rental_id() == rent_id:
                #if str(rent.get_date()) > str(ret_date):
                   #raise ServiceError("Not a valid date, date > return date !")

                if rent.get_due() < ret_date:
                    #due_date = datetime.datetime.strptime(rent.get_due(), "%d-%m-%Y")
                    #ret_date = datetime.datetime.strptime(ret_date, "%d-%m-%Y")
                    late_days = (ret_date - rent.get_due()).days
                    late_days = int(late_days)
                    rent.set_late_days(late_days)
                    self.__repoRentals.late_movies(rent)
                else:
                    #date = datetime.datetime.strptime(rent.get_date(), "%d-%m-%Y")
                    #ret_date = datetime.datetime.strptime(ret_date, "%d-%m-%Y")
                    days_numb = (ret_date - rent.get_date()).days
                    days_numb = int(days_numb)
                    movie_id = rent.get_movie_id()
                    client_id = rent.get_client_id()
                    client = self.__repoClients.getClient(client_id)
                    movie = self.__repoMovies.getMovie(movie_id)
                    movie.set_stats(days_numb)
                    client.set_stats(days_numb)

                rent.set_return_date(ret_date)
                movie_id = rent.get_movie_id()
                movie = self.__repoMovies.getMovie(movie_id)
                movie.set_availability(True)
                self.__repoRentals.remove_rental(rent)
                valid = 0
                break
        if valid == 1:
            raise ServiceError("Rental not existent !")

    def show_rent_stats(self):
        return self.__repoRentals.rental_stats()

class ServiceClients(object):

    def __init__(self, repoClients, validClients, repoUndo):
        self.__repoClients = repoClients
        self.__validClients = validClients
        self.__repoClients.generate_clients()
        self.__repoUndo = repoUndo


    def add_client(self, c_id, c_name, stats):
        client = Client(c_id, c_name, stats)
        self.__validClients.validate_client(client)
        self.__repoUndo.add_action(('add_client', client))
        self.__repoClients.add(client)

    def remove_client(self, c_id):
        client = self.__repoClients.getClient(c_id)
        self.__repoUndo.add_action(('remove_client', client))
        self.__repoClients.remove(client)

    def update_client(self, c_id, name):
        client = self.__repoClients.getClient(c_id)
        stats = client.get_stats()
        new_client = Client(c_id, name, stats)
        self.__repoUndo.add_action(('update_client', client, new_client))
        self.__repoClients.update_client(client, new_client)

    def get_clients(self):
        return self.__repoClients.get_all()

    def show_rent_stats(self):
        return self.__repoClients.client_stats()

    def search_client(self, option, string):
        if int(option) == 1:
            return self.__repoClients.search_id(string)
        elif int(option) == 2:
            return self.__repoClients.search_name(string)

class ServiceUndoRedo(object):

    def __init__(self, Undo_redo, repoMovies, repoClients, repoRentals):
        self.__repo_undo_redo = Undo_redo
        self.__repoMovies = repoMovies
        self.__repoClients = repoClients
        self.__repoRentals = repoRentals

    def redo_action(self):
        operations = {
            'add_movie': self.__repoMovies.add,
            'update_movie': self.__repoMovies.update_movie,
            'remove_movie': self.__repoMovies.remove,
            'add_client': self.__repoClients.add,
            'update_client': self.__repoClients.update_client,
            'remove_client': self.__repoClients.remove
        }
        list = self.__repo_undo_redo.get_undo_action()
        length = len(list)
        if length == 1:
            operations[list[0]]()
        elif length == 2:
            operations[list[0]](list[1])
        elif length == 3:
            operations[list[0]](list[1], list[2])


    def undo_action(self):
        operations = {
            'add_movie': self.__repoMovies.remove,
            'update_movie': self.__repoMovies.update_movie,
            'remove_movie': self.__repoMovies.add,
            'add_client': self.__repoClients.remove,
            'update_client': self.__repoClients.update_client,
            'remove_client': self.__repoClients.add
        }
        action = self.__repo_undo_redo.get_action()
        length = len(action)

        if length == 1:
            operations[action[0]]()
        elif length == 2:
            operations[action[0]](action[1])
        elif length == 3:
            operations[action[0]](action[2], action[1])
        self.__repo_undo_redo.copy_undo_action()


