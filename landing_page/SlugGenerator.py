import random, string

def slugForObjectId(objectId):
	random.seed(objectId)
	return ''.join(random.choice(string.ascii_letters + string.digits) for _ in xrange(8))