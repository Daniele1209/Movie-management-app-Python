from errors import ValidError

class movieValidator(object):

    def __init__(self):
        pass

    def validate_movie(self, movie):
        errors = ""
        if movie.get_movie_id() == "":
            errors += "invalid id !"
        if movie.get_title()=="":
            errors += "invalid title !"
        if movie.get_desc() == "":
            errors += "invalid description !"
        if movie.get_genre() == "":
            errors += "invalid genre !"

        if len(errors) > 0:
            raise ValidError(errors)

class rentalValidator(object):

    def __init__(self):
        pass

    def validate_rentals(self, rental):
        errors = ""
        if rental.get_rental_id() == "":
            errors += "invalid id !"
        if rental.get_movie_id() == "":
            errors += "invalid movie id !"
        if rental.get_client_id() == "":
            errors += "invalid client id !"
        if rental.get_date() == "":
            errors += "invalid date !"
        if rental.get_due() == "":
            errors += "invalid due date !"

        if len(errors) > 0:
            raise ValidError(errors)

class clientValidator(object):

    def __init__(self):
        pass

    def validate_client(self, client):
        errors = ""
        if client.get_client_id() == "":
            errors += "invalid id !"
        if client.get_name() == "":
            errors += "invalid name !"

        if len(errors) > 0:
            raise ValidError(errors)