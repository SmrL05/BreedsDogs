import unittest
import sys
sys.path.append("C:/Users/admin/source/repos/maria-kononova/BreedsDogs")
import feedbackPY

class FeedbackTest(unittest.TestCase):
    def test_checkPhone_valid(self):
        listvalidphone = ["+7(953)354-88-91", "7(953)354-88-91", "8(953)354-88-91"]
        for phone in listvalidphone:
            self.assertTrue(feedbackPY.checkPhone(phone))
    def test_checkPhone_notvalid(self):
        listvalidphone = ["", "fsddfs", "8(9f3)354-88-91", "9(953)354-88-91", "8(953)354-88-9",
                         "795333548891", "-7(953)354-88-91", "+7(xxx)xxx-xx-xx", "+7()354-88-91", "+7953354-88-91"]
        for phone in listvalidphone:
            self.assertFalse(feedbackPY.checkPhone(phone))