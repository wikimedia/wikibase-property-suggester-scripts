__author__ = 'virginia.weidhaas'
import MySQLdb

class UserInputEvaluator():
	def __init__(self):
		db = MySQLdb.connect("127.0.0.1","root","","my_wiki" )
		cursor = db.cursor()
		data = self.get_overall(cursor)
		print "Ausgabe"
		for i in data:
			print i

		eval = self.get_eval(cursor)
		print "Daten"
		for j in eval:
			print j
		db.close()
	def get_user_evaluations(self):
		pass

	def get_overall(self, cursor):
		cursor.execute("SELECT overall, count(overall) FROM wbs_evaluations GROUP BY overall ORDER BY overall;")
		data = cursor.fetchall()
		return data

	def get_eval(self, cursor):
		cursor.execute("SELECT suggestions from wbs_evaluations;")
		data = cursor.fetchall
		return data


x = UserInputEvaluator()