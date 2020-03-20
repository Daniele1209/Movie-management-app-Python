import operator
from Entities import Movie, Client, Rental
from errors import RepoError
import pickle
from pickle import dump

class repoMovies(object):

    @staticmethod
    def check_string(list_item, search_term):
        search_term = search_term.casefold()
        list_item = list_item.casefold()
        if str(search_term) not in str(list_item):
            return False
        else:
            return True

    def __init__(self):
        self._movie_list = []

    def size(self):
        return len(self._movie_list)

    def add(self, obj):
        if obj in self._movie_list:
            raise RepoError("Id already exists !\n")
        self._movie_list.append(obj)

    def remove(self, obj):
        if obj not in self._movie_list:
            raise RepoError("Movie not available for removing !")
        else :
            self._movie_list.remove(obj)

    def getMovie(self,id):
        valid = 1
        for movie in self._movie_list:
            if movie.get_movie_id() == id:
                return movie
        if valid == 1:
            raise RepoError("Movie does not exist !")

    def check_movie(self, movie):
        if movie not in self._movie_list:
            raise RepoError("Not a valid movie id ")

    def update_movie(self, movie, new_movie):
        if movie not in self._movie_list:
            raise RepoError("Movie not in list !")
        index = self._movie_list.index(movie)
        self._movie_list[index] = new_movie

    def get_all(self):
        return self._movie_list[:]
    #--------------SEARCHING--------------------

    def search_id(self, string):
        __search_list = []
        for movie in self._movie_list:
            m_id = movie.get_movie_id()
            if repoMovies.check_string(m_id, string):
                __search_list.append(movie)
        if len(__search_list) == 0:
            raise RepoError("Movie not found !")
        else:
            return __search_list

    def search_title(self, string):
        __search_list = []
        for movie in self._movie_list:
            title= movie.get_title()
            if repoMovies.check_string(title, string):
                __search_list.append(movie)
        if len(__search_list) == 0:
            raise RepoError("Movie not found !")
        else:
            return __search_list

    def search_desc(self, string):
        __search_list = []
        for movie in self._movie_list:
            desc = movie.get_desc()
            if repoMovies.check_string(desc, string):
                __search_list.append(movie)
        if len(__search_list) == 0:
            raise RepoError("Movie not found !")
        else:
            return __search_list

    def search_genre(self, string):
        __search_list = []
        for movie in self._movie_list:
            genre = movie.get_genre()
            if repoMovies.check_string(genre, string):
                __search_list.append(movie)
        if len(__search_list) == 0:
            raise RepoError("Movie not found !")
        else:
            return __search_list

    def delete_list(self):
        self._movie_list.clear()

    #---------------STATS---------------

    def movie_stats(self):
        if len(self._movie_list) != 0:
            top_list = sorted(self._movie_list, key=lambda obj:obj.get_movie_stats(), reverse = True)
            return top_list
        else:
            raise RepoError("Can not do a top because movie list is empty !")

    #----------------GENERATE-------------
    def generate_movies(self):
        file = open("Random/Movies.txt", "r")
        movies = file.readlines()
        file.close()
        for movie in movies:
            movie = movie.split(",")
            m_id = movie[0]
            m_title = movie[1]
            m_desc = movie[2]
            m_genre = movie[3]
            self._movie_list.append(Movie(m_id, m_title, m_desc, m_genre, True, 0))

class repoClients(object):

    def __init__(self):
        self._client_list = []

    def size(self):
        return len(self._client_list)

    def add(self, obj):
        if obj in self._client_list:
            raise RepoError("Id already exists !\n")
        self._client_list.append(obj)

    def remove(self, obj):
        if obj not in self._client_list:
            raise RepoError("Client not available for removing !")
        else :
            self._client_list.remove(obj)

    def getClient(self,id):
        valid = 1
        for client in self._client_list:
            if client.get_client_id() == id:
                valid = 0
                return client
        if valid == 0:
            raise RepoError("Client does not exist !")

    def check_client(self, client):
        if client not in self._client_list:
            raise RepoError("Not a valid client id ! ")

    def update_client(self,client, new_client):
        if client not in self._client_list:
            raise RepoError("Client not in list !")
        index = self._client_list.index(client)
        self._client_list[index] = new_client

    def get_all(self):
        return self._client_list[:]
    #---------------SEARCH---------------

    def search_id(self, string):
        __search_list = []
        for client in self._client_list:
            c_id = client.get_client_id()
            if repoMovies.check_string(c_id, string):
                __search_list.append(client)
        if len(__search_list) == 0:
            raise RepoError("Client not found !")
        else:
            return __search_list

    def search_name(self, string):
        __search_list = []
        for client in self._client_list:
            name = client.get_name()
            if repoMovies.check_string(name, string):
                __search_list.append(client)
        if len(__search_list) == 0:
            raise RepoError("Client not found !")
        else:
            return __search_list

    def delete_list(self):
        self._client_list.clear()

    #-----------------STATS-----------------

    def client_stats(self):
        if len(self._client_list) != 0:
            top_list = sorted(self._client_list, key = lambda obj:obj.get_stats(), reverse = True)
            return top_list
        else:
            raise RepoError("Can not do a top because client list is empty !")

    #----------------GENERATE-------------
    def generate_clients(self):
        file = open("Random/Clients.txt", "r")
        clients = file.readlines()
        file.close()
        for client in clients:
            client = client.split(",")
            c_id = client[0]
            c_name = client[1]
            self._client_list.append(Client(c_id, c_name, 0))

class repoRentals(object):

    def __init__(self):
        self._rental_list = []
        self._late_rental = []

    def get_rentals(self):
        return self._rental_list

    def get_all(self):
        return self._rental_list[:]

    def verify_valid(self, client_id, date):
        for rent in self._rental_list:
            if rent.get_client_id() == client_id:
                if str(rent.get_due()) < str(date):
                    raise RepoError("Client has passed their due date for a rented movie !")

    def remove_rental(self, rent):
            self._rental_list.remove(rent)

    def add_rental(self, rental):
        if rental in self._rental_list:
            raise RepoError("Rental already in list")
        self._rental_list.append(rental)

    def rental_stats(self):
        if len(self._late_rental) != 0:
            top_list = sorted(self._late_rental, key = lambda obj:obj.get_late_days(), reverse = True)
            return top_list
        else:
            raise RepoError("Can not do a top because rental list is empty !")

    def late_movies(self, rental):
        self._late_rental.append(rental)

    #------------GENERATE---------------

    def generate_rentals(self):
        pass
        """ 
        file = open("Random/Rentals.txt", "r")
        rentals = file.readlines()
        file.close()
        for rental in rentals:
            rental = rental.split(",")
            r_id = rental[0]
            m_id = rental[1]
            c_id = rental[2]
            r_date = rental[3]
            r_due = rental[4]
            self._rental_list.append(Rental(r_id, m_id, c_id, r_date, r_due, None, 0))
    """

class Undo_redo(object):
    #add , remove, update, rent, return
    def __init__(self):
        self.__undo_list = []
        self.__redo_list = []

    def get_action(self):
        if len(self.__redo_list) == 0:
            raise RepoError("can not undo anymore !")
        else:
            return self.__redo_list[-1]

    def add_action(self, action):
        self.__redo_list.append(action)

    def copy_undo_action(self):
        self.__undo_list.append(self.__redo_list[-1])
        self.__redo_list.pop()

    def get_undo(self):
        return self.__undo_list[:]

    def get_undo_action(self):
        if len(self.__undo_list) == 0:
            raise RepoError("No undo operations were performed ! ")
        else:
            return self.__undo_list[-1]

class pickle_repoMovies(object):

    def __init__(self, file):
        self.__file = file

    def __load_movies(self):
        file = open (self.__file, "rb")
        try:
            movie_list = pickle.load(file)
        except Exception:
            movie_list = []
        file.close()
        return movie_list[:]

    def __store(self, movie_list):
        file = open(self.__file, "wb")
        pickle.dump(movie_list, file)
        file.close()

    def size(self, movie_list):
        return len(movie_list)

    def add(self, obj):
        movies = self.__load_movies()
        if obj in movies:
            raise RepoError("Movie already in list !")
        movies.append(obj)
        self.__store(movies)

    def remove(self, obj):
        movies = self.__load_movies()
        if obj not in movies:
            raise RepoError("Movie not in list !")
        for i in range(len(movies)):
            if movies[i] == obj:
                del movies[i]
                break
        self.__store(movies)

    def getMovie(self,id):
        movies = self.__load_movies()
        for movie in movies:
            if movie.getID() == id:
                return movie
        raise RepoError("Movie not in list! ")

    def update_movie(self, movie, new_movie):
        movies = self.__load_movies()
        if movie not in movies:
            raise RepoError("Movie does not exist ! ")
        for i in range(len(movies)):
            if movies[i] == movie:
                movies[i] = new_movie
                break
        self.__store(movies)

    def get_all(self):
        movies = self.__load_movies()
        return  movies[:]

    def generate_movies(self):
        pass

class file_repoMovies:

    def __init__(self,file):
        self.__file = file

    def __load_movies(self):
        file = open (self.__file, "r")
        movies = file.readlines()
        movie_list = []
        for movie in movies :
            movie.strip()
            movie = movie.replace("\n", "")
            movie = movie.split(",")
            movie_list.append(Movie(str(movie[0]),str(movie[1]),str(movie[2]),str(movie[3]),bool(movie[4]),int(movie[5])))
        file.close()
        return movie_list

    def __store(self, movie_list):
        file = open(self.__file, "w")
        for movie in movie_list:
            file.write(str(movie.get_movie_id() + "," + movie.get_title() + "," + movie.get_desc() + "," + movie.get_genre() + "," + movie.get_availability() + "," + movie.get_movie_stats()+"\n"))
        file.close()

    def size(self, movie_list):
        return len(movie_list)

    def add(self, obj):
        movies = self.__load_movies()
        if obj in movies:
            raise RepoError("Movie already in list ! ")
        movies.append(obj)
        self.__store(movies)


    def remove(self, obj):
        movies = self.__load_movies()
        if obj not in movies:
            raise RepoError("Movie not in list !")
        for i in range(len(movies)):
            if movies[i] == obj:
                del movies[i]
                break
        self.__store(movies)

    def getMovie(self,id):
        movies = self.__load_movies()
        for movie in movies:
            if movie.get_movie_id() == id:
                return movie
        raise RepoError("Movie not in list! ")

    def update_movie(self, movie, new_movie):
        movies = self.__load_movies()
        if movie not in movies:
            raise RepoError("Movie does not exist ! ")
        for i in range(len(movies)):
            if movies[i] == movie:
                movies[i] = new_movie
                break
        self.__store(movies)

    def get_all(self):
        movies = self.__load_movies()
        movie_list = []
        for movie in range(0,len(movies)):
            movie_list.append(movies[movie])
        return movie_list[:]

    def generate_movies(self):
        pass

class pickle_repoClients(object):

    def __init__(self, file):
        self.__file = file

    def __load_clients(self):
        file = open (self.__file, "rb")
        try:
            client_list = pickle.load(file)
        except Exception:
            client_list = []
        file.close()
        return client_list[:]

    def __store(self, client_list):
        file = open(self.__file, "wb")
        pickle.dump(client_list, file)
        file.close()

    def size(self, client_list):
        return len(client_list)

    def add(self, obj):
        clients = self.__load_clients()
        if obj in clients:
            raise RepoError("Client already in list !")
        clients.append(obj)
        self.__store(clients)

    def remove(self, obj):
        clients = self.__load_clients()
        if obj not in clients:
            raise RepoError("Client not in list !")
        for i in range(len(clients)):
            if clients[i] == obj:
                del clients[i]
                break
        self.__store(clients)

    def getClient(self,id):
        clients = self.__load_clients()
        for client in clients:
            if client.get_client_id() == id:
                return client
        raise RepoError("Client not in list! ")

    def update_client(self, client, new_client):
        clients = self.__load_clients()
        if client not in clients:
            raise RepoError("Client does not exist ! ")
        for i in range(len(clients)):
            if clients[i] == client:
                client[i] = new_client
                break
        self.__store(clients)

    def get_all(self):
        movies = self.__load_clients()
        return  movies[:]

    def generate_clients(self):
        pass

class file_repoClients:

    def __init__(self,file):
        self.__file = file

    def __load_clients(self):
        file = open (self.__file, "r")
        clients = file.readlines()
        client_list = []
        for client in clients :
            client.strip()
            client = client.replace("\n", "")
            client = client.split(",")
            client_list.append(Client(str(client[0]),str(client[1]),int(client[2])))
        file.close()
        return client_list

    def __store(self, client_list):
        file = open(self.__file, "w")
        for client in client_list:
            file.write(str(client.get_client_id()) + "," + str(client.get_name()) + "," + str(client.get_stats())+"\n")
        file.close()

    def size(self, client_list):
        return len(client_list)

    def add(self, obj):
        clients = self.__load_clients()
        if obj in clients:
            raise RepoError("Client already in list ! ")
        clients.append(obj)
        self.__store(clients)


    def remove(self, obj):
        clients = self.__load_clients()
        if obj not in clients:
            raise RepoError("Client not in list !")
        for i in range(len(clients)):
            if clients[i] == obj:
                del clients[i]
                break
        self.__store(clients)

    def getClient(self,id):
        clients = self.__load_clients()
        for client in clients:
            if client.get_client_id() == id:
                return client
        raise RepoError("Client not in list! ")

    def update_client(self, client, new_client):
        clients = self.__load_clients()
        if client not in clients:
            raise RepoError("Client does not exist ! ")
        for i in range(len(clients)):
            if clients[i] == client:
                clients[i] = new_client
                break
        self.__store(clients)

    def get_all(self):
        clients = self.__load_clients()
        client_list = []
        for client in range(0,len(clients)):
            client_list.append(clients[client])
        return client_list[:]

    def generate_clients(self):
        pass