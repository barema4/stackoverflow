class Questions(object):
	"""docstring for ClassName"""
	def __init__(self, id, title, body, user_name):
                self.id = id
                self.title = title
                self.body = body
                self.user_name = user_name

class Solutions(object):
        def __init__(self, answer_id, question_id, body):
                self.answer_id = answer_id
                self.question_id = question_id
                self.body = body
        
        
     