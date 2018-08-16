
from views import Questions
class Urls:
    
    @staticmethod
    def generate(app):
        """
        Generate urls on the app context
        It takes no argument
        :param: app: takes in the app variable
        :return: urls
        """
       
        app.add_url_rule('/api/v1/questions/<int:id>', view_func=Questions.as_view('h'), methods=['GET',])
      