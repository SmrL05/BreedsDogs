import unittest
import article

class ArticlesTest(unittest.TestCase):
    def test_isCorrectData_incorrectMail_equal(self):
        #arrange
        expected = False
        #act
        act = article.isCorrectData("2@f.r", "email")
        #assert
        self.assertEqual(expected, act)

    def test_isCorrectData_incorrectMail_equal2(self):
        #arrange
        expected = False
        #act
        act = article.isCorrectData("@.@.ru", "email")
        #assert
        self.assertEqual(expected, act)

    def test_isCorrectData_correctMail_equal3(self):
        #arrange
        expected = True
        #act
        act = article.isCorrectData("test_mail@yandex.ru", "email")
        #assert
        self.assertEqual(expected, act)

    def test_isCorrectData_incorrectPhone_equal(self):
        #arrange
        expected = False
        #act
        act = article.isCorrectData("+7893", "phone")
        #assert
        self.assertEqual(expected, act)

    def test_isCorrectData_incorrectPhone_equal2(self):
        #arrange
        expected = False
        #act
        act = article.isCorrectData("123456789012345", "phone")
        #assert
        self.assertEqual(expected, act)

    def test_isCorrectData_correctPhone_equal3(self):
        #arrange
        expected = True
        #act
        act = article.isCorrectData("+79962209547", "phone")
        #assert
        self.assertEqual(expected, act)

    def test_isCorrectData_correctPhone_equal4(self):
        #arrange
        expected = True
        #act
        act = article.isCorrectData("89962209547", "phone")
        #assert
        self.assertEqual(expected, act)

    def test_isCorrectData_correctPhone_equal5(self):
        #arrange
        expected = True
        #act
        act = article.isCorrectData("+7(996)220-95-47", "phone")
        #assert
        self.assertEqual(expected, act)