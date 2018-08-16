from spy import Questions


class Urls:

    @staticmethod
    def generate(app):
        """
        Generate urls on the app context
        
        """
        app.add_url_rule('/api/v1/questions/<int:Id>/answers', view_func=Questions.as_view('r'), methods=['POST',])

