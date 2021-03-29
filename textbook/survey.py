class AnonymousSurvey:
    """Collects anonymous answers to survey questions"""

    def __init__(self, question):
        """Initializing the class attributes"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Displays the survey question"""
        return self.question

    def store_response(self, new_response):
        """Saves the answer of each user"""
        self.responses.append(new_response)

    def show_results(self):
        """Displays the results of the survey"""
        for response in self.responses:
            print(f' {response}')
