import unittest
from survey import AnonymousSurvey

question = "What is the name of the president of the United States? "


class TestAnonymousClass(unittest.TestCase):
    """Tests the implementations of class Anonymous survey"""

    def test_show_question(self):
        """Testing that the question returned is equal to the one i used to
        initialize the class"""
        survey = AnonymousSurvey(question)
        self.assertEqual(question, "What is the name of the president of the United States? ")
        answer = "Joe Biden"
        survey.store_response(answer)
        self.assertIn(answer, survey.responses)

    def test_show_three_question(self):
        """Testing that the question returned is equal to the one i used to
        initialize the class"""
        survey = AnonymousSurvey(question)
        self.assertEqual(question, "What is the name of the president of the United States? ")
        answer = ["Joe Biden", "Barack Obama", "Donald Trump", "Bill Gate"]
        for ans in answer:
            survey.store_response(ans)
        for ans in survey.responses:
            self.assertIn(ans, survey.responses)


if __name__ == '__main__':
    unittest.main()
