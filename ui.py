from errors import ValidError, RepoError
import datetime

class UI(object):

    @staticmethod
    def print_all(objects):
        x = 0
        for obj in objects:
            x += 1
            print('{} -  {}'.format(x,obj))
        print()

    @staticmethod
    def input_date():
       # try:
       #     datetime.datetime.strptime(date, '%d-%m-%Y').strftime('%d-%m-%Y')
       # except : raise ValidError("Ïncorrect data format, it should be DD-MM-YYYY !")
        day = int(input("Day: "))
        month = int(input("Month: "))
        year = int(input("Year: "))
        return day,month, year


    def __ui_add(self):
        print("1 : Movie")
        print("2: Client")
        option = int(input())
        if option == 1:
            m_id = input("Enter movie id: ")
            m_title = input("Enter movie title: ")
            m_desc = input("Enter description: ")
            m_genre = input("Enter movie genre: ")
            availability = True
            stats = 0
            self.__movie_services.add_movie(m_id, m_title, m_desc, m_genre,availability, stats)

        elif option == 2:
            c_id = input("Enter client id: ")
            c_name = input("Enter client name: ")
            stats = 0
            self.__client_services.add_client(c_id, c_name, stats)

        else :
            raise ValidError("Not a valid option !\n")

    def __ui_remove(self):
        print("1 : Movie")
        print("2 : Client")
        option = int(input())
        if option == 1:
            m_id = input("Enter the id of the movie: ")
            self.__movie_services.remove_movie(m_id)

        elif option == 2:
            c_id = input("Enter the id of the client: ")
            self.__client_services.remove_client(c_id)

        else:
            raise ValidError("Not a valid option !\n")

    def __ui_update(self):
        print("1 : Movie")
        print("2 : Client")
        option = input()
        if int(option) == 1:
            m_id = input("Enter the id of the movie: ")
            title = input("New title: ")
            description = input("New description: ")
            genre = input("New genre: ")
            print("Available or not 1. true / 2. false:")
            availability = input()
            if int(availability) == 1:
                availability = True
            elif int(availability) == 2:
                availability = False
            else:
                raise ValidError("Not a valid option !\n")
            self.__movie_services.update_movie(m_id,title, description, genre, availability)

        elif int(option) == 2:
            c_id = input("Enter the id of the client: ")
            name = input("New name: ")
            self.__client_services.update_client(c_id,name)

        else:
            raise ValidError("Not a valid option !\n")

    def __ui_print(self):
        __movieList = self.__movie_services.get_movies()
        __clientsList = self.__client_services.get_clients()
        UI.print_all(__movieList)
        print("\n")
        UI.print_all(__clientsList)


    def __ui_print_rentals(self):
        rentedList = self.__rental_services.get_rentals()
        UI.print_all(rentedList)

    def __ui_rent(self):
        __rental_id = input("Enter the rental id: ")
        __movie_id = input("Enter the movie id: ")
        __client_id = input("Enter the client id: ")
        day, month, year = __date = UI.input_date()
        date = datetime.date(year, month, day)
        day, month, year = __due_date = UI.input_date()
        due = datetime.date(year, month, day)


        self.__rental_services.rent_movie(__rental_id,__movie_id, __client_id, date, due)

    def __ui_search(self):
        print("1 : Movie")
        print("2 : Client")
        __option = input()
        if int(__option) == 1:
            print("Search by: 1- ID  2- Title  3- Description  4- Genre  : ")
            __option_2 = input()
            if int(__option_2) == 1 or int(__option_2) == 2 or int(__option_2) == 3 or int(__option_2) == 4:
                __string = input("Search : ")
                movies = self.__movie_services.search_movie(__option_2, __string)
                UI.print_all(movies)
            else:
                raise ValidError("Not a valid option ! ")

        elif int(__option) == 2:
            print("Search by: 1- ID  2- Name  : ")
            __option_2 = input()
            if int(__option_2) == 1 or int(__option_2)== 2:
                __string = input("Search : ")
                clients = self.__client_services.search_client(__option_2, __string)
                UI.print_all(clients)
            else:
                raise ValidError("Not a valid option ! ")

        else:
            raise ValidError("Not a valid option !\n")


    def __ui_return(self):
        __movie_id = input("Enter the rent id: ")
        day, month, year = UI.input_date()
        date = datetime.date(year, month, day)
        self.__rental_services.return_movie(__movie_id, date)

    def __ui_m_stats(self):
        stats_list = self.__movie_services.show_rent_stats()
        UI.print_all(stats_list)

    def __ui_c_stats(self):
        stats_list = self.__client_services.show_rent_stats()
        UI.print_all(stats_list)

    def __ui_late_stats(self):
        stats_list = self.__rental_services.show_rent_stats()
        UI.print_all(stats_list)

    def __ui_undo(self):
        self.__undo_redo_services.undo_action()

    def __ui_redo(self):
        self.__undo_redo_services.redo_action()

    def __print_commands(self):
        print("1 - add        6 - print                     11 - show late rentals stats")
        print("2 - remove     7 - print rentals             12 - undo")
        print("3 - update     8 - search                    13 - redo")
        print("4 - rent       9 - show movie statistics")
        print("5 - return     10 - show client statistics")

    def __init__(self, movie_services, client_services, rental_services, undo_redo_services):
        self.__movie_services = movie_services
        self.__client_services = client_services
        self.__rental_services = rental_services
        self.__undo_redo_services = undo_redo_services


        self.__commands = {
            "1": self.__ui_add,
            "2": self.__ui_remove,
            "3": self.__ui_update,
            "4": self.__ui_rent,
            "5": self.__ui_return,
            "6": self.__ui_print,
            "7": self.__ui_print_rentals,
            "8": self.__ui_search,
            "9": self.__ui_m_stats,
            "10": self.__ui_c_stats,
            "11": self.__ui_late_stats,
            "12": self.__ui_undo,
            "13": self.__ui_redo
        }

    def run(self):

        while True:
            self.__print_commands()
            cmd = input(">>>")
            if cmd == "exit":
                return
            if cmd in self.__commands:
                try:
                    self.__commands[cmd]()
                except ValueError as er:
                    print("ui error:\n"+str(er))
                except ValidError as err:
                    print("valid error:\n"+str(err))
                except RepoError as errr:
                    print("repo error:\n"+str(errr))
            else:
                print("Invalid command !\n")

