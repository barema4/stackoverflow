from flask.views import MethodView
from flask import Flask, request, Response

from flask import jsonify


class Questions(MethodView):
    Answers = [
        {"user_name": "sam", "Description": "What is html", "answer": "","id": 1},
        {"user_name": "Derick", "Description": "what is data structure", "answer": "", "id": 2},
        {"user_name": "jacob", "Description": "what is javascript", "answer": "", "id": 3},
    ]

    def post(self, Id ):
        """
        method for all post answers
        """
        if not request.json:
            return jsonify({'error': "not a json request"}), 400
        else:
            Answer = {'user_name': request.json['user_name'], 'Description': request.json['Description'], 'answer': request.json['answer'],
                        'id': request.json['id']}
            self.Answers.append(Answer)
            return jsonify({'Answers': self.Answers})

    #req,