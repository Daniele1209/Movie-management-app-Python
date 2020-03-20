#add remoove, update
import datetime

class Movie(object):  # movie id, title, decription , genre

    def __init__(self, movie_id, title, desc, genre,availability, stats):
        self.__movie_id = movie_id
        self.__title = title
        self.__desc = desc
        self.__genre = genre
        self.__availability = availability
        self.__stats = stats

    def get_movie_id(self):
        return self.__movie_id

    def get_title(self):
        return self.__title

    def get_desc(self):
        return self.__desc

    def get_genre(self):
        return self.__genre

    def get_availability(self):
        return self.__availability

    def set_availability(self, state):
        self.__availability = state

    def get_movie_stats(self):
        return self.__stats

    def set_stats(self, other):
        stats = int(self.__stats)
        stats += int(other)
        self.__stats = stats

    def __eq__(self, other):
        return self.__movie_id == other.__movie_id

    def __str__(self):
        if self.__availability == True:
            ava = "Available"
        else:
            ava = "Not available"
        return str(self.__movie_id)+" | "+self.__title+" | "+self.__desc+" | "+self.__genre+" | "+ava+" | "+str(self.__stats)


class Client(object):  # client id , name

    def __init__(self, client_id, name, stats):
        self.__client_id = client_id
        self.__name = name
        self.__stats = stats

    def get_client_id(self):
        return self.__client_id

    def get_name(self):
        return self.__name

    def get_stats(self):
        return self.__stats

    def set_stats(self, other):
        stats = int(self.__stats)
        stats += int(other)
        self.__stats = stats

    def __eq__(self, other):
        return self.__client_id == other.__client_id

    def __str__(self):
        return str(self.__client_id)+" | "+self.__name+" | "+str(self.__stats)


class Rental(object):  # rentalid, movieid, clientid, rented date, due date, return date

    def __init__(self,rental_id, movie_id, client_id, rented_date, due_date, return_date, late_days):
        self.__rental_id = rental_id
        self.__movie_id = movie_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__due_date = due_date
        self.__return_date = return_date
        self.__late_days  = late_days

    def get_rental_id(self):
        return self.__rental_id

    def get_movie_id(self):
        return self.__movie_id

    def get_client_id(self):
        return self.__client_id

    def get_date(self):
        return self.__rented_date

    def get_due(self):
        return self.__due_date

    def get_return(self):
        return self.__return_date

    def set_return_date(self, date):
        self.__return_date = date

    def get_late_days(self):
        return self.__late_days

    def set_late_days(self, other):
        days = int(self.__late_days)
        days += int(other)
        self.__late_days = days

    def __eq__(self, other):
        return self.__rental_id == other.__rental_id

    def __str__(self):
        return str(self.__rental_id)+" | "+str(self.__movie_id)+" | "+str(self.__client_id)+" | "+str(self.__rented_date)+" | "+str(self.__due_date)+" | "+str(self.__return_date)
