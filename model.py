import boto.dynamodb

from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey

#users = Table.create('users', schema=[HashKey('username')]);
def getItems():

	conn = boto.dynamodb.connect_to_region(
				'eu-west-1',
				aws_access_key_id='AKIAII7YEALV37GRSGSA',
				aws_secret_access_key='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')

	#print conn.list_tables()

	table = conn.get_table('test1')

	#print  conn.describe_table('test1')

	#item = table.get_item(hash_key='[B@77b3bf0d')

	items = table.scan()

	return items

#for i in getItems():
#	print i

#table = Table('test1')

#data = table.get_item(id='[B@77b3bf0d')

#alltable = users.scan()

#print alltable
#for item in getItems():
#	print item