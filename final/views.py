
""" This module defines views """
from flask import jsonify, request
from flask.views import MethodView
from viewclass import Questions
from viewclass import Solutions
class GetQuestion(MethodView):
    """
    This class  defines views
    """
    questions1 = Questions(1, 'html', 'what is the meaning of h6', 'john')
    
    questions2 = Questions(2, 'form', 'how to implement search button', 'David')
    
    questions3 = Questions(3, 'data structures', 'what is stack', 'sam')

    questions4 = Questions(4, 'java', 'what is a class', 'jacob')
    questions = []
    questions = [questions1, questions2, questions3, questions4]

    solutions1 = Solutions(1, 3, 'programing problem')
    solutions2 = Solutions(4, 5,'html 5')
    solutions = []
    solutions = [solutions1, solutions2]
   
 
    
    
    def get(self, question_id):
        """
        method for all get requests
        """
        if question_id == None:
            return jsonify({'questions':[question.__dict__ for question in self.questions]})
        quest = [question.__dict__ for question in self.questions if question.__dict__['id'] == question_id]
        return jsonify({'question' : quest[0]})    
    
    def post(self, question_id):
        """
        method for all post requests
        """
        
        if question_id is None:
             question = Questions(request.json['id'], request.json['title'], request.json['body'], request.json['user_name'])
             self.questions.append(question)
             return jsonify({'questions' :  [question.__dict__ for question in self.questions]})

        answer = Solutions(request.json['answer_id'], 'question_id', request.json['body'])
        self.solutions.append(answer)
        return jsonify({'solutions' :  [solution.__dict__ for solution in self.solutions]})
