from flask.views import MethodView
from flask import Flask, request, Response

from flask import jsonify


class Questions(MethodView):
    questions = [
        {"user_name": "sam", "Description": "What is html", "id": 1},
        {"user_name": "Derick", "Description": "what is data structure", "id": 2},
        {"user_name": "jacob", "Description": "what is javascript", "id": 3},
    ]

    def post(self ):
        """
        method for all post requests
        """
        if not request.json:
            return jsonify({'error': "not a json request"}), 400
        else:
            question = {'user_name': request.json['user_name'], 'Description': request.json['Description'],
                        'id': request.json['id']}
            self.questions.append(question)
            return jsonify({'questions': self.questions})

    #req = {'user_name': request.json['user_name'], 'Description': request.json['Description'], 'id': request.json['id']}
    #self.questions.append(req)
     #  return jsonify({'requests': self.questions}
