from ui import UI
from repo import repoMovies, repoClients, repoRentals, Undo_redo, pickle_repoMovies, file_repoMovies, file_repoClients, pickle_repoClients
from services import ServiceMovies, ServiceClients, ServiceRentals, ServiceUndoRedo
#from tests import test_first_function_repo, test_first_function_services
from validator import movieValidator, clientValidator, rentalValidator
from settings import Settings
"""
tests_repo = test_first_function_repo()
tests_services = test_first_function_services()
tests_repo.run_all_tests()
tests_services.run_all_tests()
"""
settings = Settings("settings.properties")
configuration = settings.configurations()
memo = False

if str(configuration[0]) == "inmemory":
    repoMovies = repoMovies()
    repoClients = repoClients()
    repoRentals = repoRentals()
elif str(configuration[0]) == "textfiles":
    repoMovies = file_repoMovies(configuration[1])
    repoClients = file_repoClients(configuration[2])
    repoRentals = repoRentals()
elif str(configuration[0]) == "binaryfiles":
    repoMovies = pickle_repoMovies(configuration[1])
    repoClients = pickle_repoClients(configuration[2])
    repoRentals = repoRentals()

movieValidator = movieValidator()
clientValidator = clientValidator()

repoUndo = Undo_redo()
ServiceMovies = ServiceMovies(repoMovies, movieValidator, repoUndo)
ServiceClients = ServiceClients(repoClients, clientValidator,repoUndo)
ServiceRentals = ServiceRentals(repoRentals, rentalValidator,  repoMovies, repoClients, repoUndo)
ServiceUndoRedo = ServiceUndoRedo(repoUndo, repoMovies, repoClients, repoRentals)
ui = UI(ServiceMovies, ServiceClients, ServiceRentals, ServiceUndoRedo)
ui.run()


