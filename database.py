from marvel import getMarvels
from cassandra.cluster import Cluster
cluster = Cluster()


session = cluster.connect("simplex")




#rows = session.execute('SELECT name, age, email FROM users')
#for user_row in rows:
#    print user_row.name, user_row.age, user_row.email
def populate():

	for marvel in getMarvels():
			print marvel['name']
			if len(marvel['description']) == 0:
				marvel['description'] = 'null'
			print marvel['description']

			print marvel['comics']['available']

			session.execute(
			    """
			    INSERT INTO marvels2 (name, description, available)
			    VALUES (%s, %s, %s)
			    """,
			    (marvel['name'], marvel['description'], str(marvel['comics']['available']))
			)


def getMarvel():

	res = [] 
	rows = session.execute("""
		SELECT * FROM marvels2 
		""")
	for user_row in rows:
		marvel ={}
		#print user_row.name, user_row.description, user_row.available
		marvel['name']= user_row.name
		marvel['description']= user_row.description
		marvel['available']= user_row.available
		res.append(marvel)

	return res



