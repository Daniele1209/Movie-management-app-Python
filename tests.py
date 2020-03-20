from Entities import *
from services import *
from repo import *
from validator import *
import unittest

class test_first_function_repo(unittest.TestCase):

    def test_add_movie(self):
        repo = repoMovies()
        repo.delete_list()
        m1 = Movie("0000", "Movie1", "Nice one", "action", True, None)
        m2 = Movie("0001", "Movie2", "Meh", "animation", True, None)
        m3 = Movie("0001", "Movie3", "Could be better", "comedy", True, None)
        m4 = Movie("0011", "Movie4", "Garbage", "drama", True, None)

        repo.add(m1)
        repo.add(m2)
        try:
            repo.add(m3)
            self.assertFalse(repo.add(m3),True)
        except :
            pass

        repo.add(m4)
        self.assertEqual(repo.get_all(), [m1,m2,m4])

    def test_add_client(self):
        repo = repoClients()
        repo.delete_list()
        c1 = Client("0000", "Name1", None)
        c2 = Client("0000", "Name2", None)
        c3 = Client("0001", "Name3", None)

        repo.add(c1)
        try:
            repo.add(c2)
            self.assertFalse(repo.add(c2), True)
        except:
            pass
        repo.add(c3)
        self.assertEqual(repo.get_all(),[c1,c3])


    def test_remove_movie(self):
        repo = repoMovies()
        repo.delete_list()
        m1 = Movie("0000", "Movie1", "Nice one", "action", True, None)
        m2 = Movie("0001", "Movie2", "Meh", "animation", True, None)
        m3 = Movie("0010", "Movie3", "Could be better", "comedy", True, None)
        repo.add(m1)
        repo.add(m2)
        repo.remove(m1)
        self.assertEqual(repo.get_all(),[m2])
        try:
            repo.remove(m3)
            self.assertFalse(repo.remove(m3), True)
        except:
            pass

    def test_remove_client(self):
        repo = repoClients()
        repo.delete_list()
        c1 = Client("0000", "Name1", None)
        c2 = Client("0001", "Name2", None)
        c3 = Client("0010", "Name3", None)
        repo.add(c1)
        repo.add(c2)
        repo.remove(c1)
        self.assertEqual(repo.get_all(),[c2])
        try:
            repo.remove(c3)
            self.assertFalse(repo.remove(c3), True)
        except:
            pass

    def test_update_movie(self):
        repo = repoMovies()
        repo.delete_list()
        m1 = Movie("0000", "Movie1", "Nice one", "action", True, None)
        m2 = Movie("0001", "Movie2", "Meh", "animation", True, None)
        new_m = Movie("0011", "Movie3", "Mehh", "anime", True, None)
        repo.add(m1)
        repo.update_movie(m1,new_m)
        try:
            repo.update_movie(m2, new_m)
            self.assertFalse(repo.update_movie(m2,new_m),True )
        except:
            pass

    def test_update_client(self):
        repo = repoClients()
        repo.delete_list()
        c1 = Client("0000", "Name1", None)
        c2 = Client("0001", "Name2", None)
        new_c = Client("0010", "Name3", None)
        repo.add(c1)
        repo.update_client(c1,new_c)
        try:
            repo.update_client(c2, new_c)
            self.assertFalse(repo.update_client(c2,new_c),True)
        except:
            pass

    def run_all_tests(self):
        self.test_add_movie()
        self.test_add_client()
        self.test_remove_movie()
        self.test_remove_client()
        self.test_update_movie()
        self.test_update_client()

class test_first_function_services(unittest.TestCase):

    def test_add_movie(self):
        service = ServiceMovies(repoMovies, movieValidator)
        try:
            service.add_movie("1209","title", "", "genre", True, None)
            self.assertFalse(service.add_movie("1209","title", "", "genre", True, None),True)
        except:
            pass

    def test_add_client(self):
        service = ServiceClients(repoClients, clientValidator)
        try:
            service.add_client("1209","", None)
            self.assertFalse(service.add_client("1209","", None),True)
        except:
            pass

    def run_all_tests(self):
        self.test_add_movie()
        self.test_add_client()
