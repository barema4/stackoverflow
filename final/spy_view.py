""" This module provides class-based views inspired by the ones in flask."""
from flask import jsonify
from flask.views import MethodView
from flask import Flask, request
class Questions(MethodView):
    """A class-based view that dispatches request methods to the corresponding
       class methods. For example, if you implement a ``get`` method, it will be
       used to handle ``GET`` requests. :
    """
    questions = [
        {"user_name": "sam", "Description": "What is html", "question_id": 1},
        {"user_name": "Derick", "Description": "what is data structure", "question_id": 2},
        {"user_name": "jacob", "Description": "what is javascript", "question_id": 3},
        ]


    def get(self, question_id=None):
        """
        method for all get requests
        """

        if 'question_id' == None:
            return jsonify({'question': [question for question in self.questions]})
        quest = [question for question in self.questions if question['question_id'] == question_id]
        return jsonify({'question': quest[0]})

    def post(self):
        """
        method for all post requests
        """

        if not request.json:
            return jsonify({'error': "not a json request"}), 400
        else:
            question = {'user_name': request.json['user_name'],
                        'Description': request.json['Description'],
                        'question_id': request.json['question_id']}
            self.questions.append(question)
            return jsonify({'questions': self.questions}), 201

class SpecificAnswer(MethodView):
    """
        class for all post requests
        """
    Answers = [
        {"user_name": "sam", "Description": "What is html", "answer": "", "question_id": 1},
        {"user_name": "Derick", "Description": "what is data structure",
         "answer": "", "question_id": 2},
        {"user_name": "jacob", "Description": "what is javascript", "answer": "", "question_id": 3},
    ]
    def post(self, question_id):
        """
        method for  post requests
        """

        if not request.json:

            return jsonify({'error': "not a json request"}), 400

        else:

            answer = {'user_name': request.json['user_name'],
                      'Description': request.json['Description'],
                      'answer': request.json['answer'],
                      'question_id': request.json['question_id']}


            self.Answers.append(answer)

            return jsonify({'Answers': self.Answers})
