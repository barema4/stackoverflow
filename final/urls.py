from spy_view import Questions, SpecificAnswer


class Urls:

    @staticmethod
    def generate(app):

        """
        Generate urls on the app context
        It takes no argument
        :param: app: takes in the app variable
        :return: urls
        """

        app.add_url_rule('/api/v1/questions/<int:question_id>', view_func=Questions.as_view('h'), methods=['GET', ])
        app.add_url_rule('/api/v1/questions/', view_func=Questions.as_view('g'), methods=['GET', ])
        app.add_url_rule('/api/v1/questions', view_func=Questions.as_view('w'), methods=['POST', ])
        app.add_url_rule('/api/v1/questions/<int:question_id>/answers', view_func= SpecificAnswer.as_view('answer'), methods=['POST', ])

