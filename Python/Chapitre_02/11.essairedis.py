import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.set('uno', 'due')
print(r.get('uno'))

d = {"nom": "Le Docteur", "Origine": "Gallifrey", "Race": "Maître du temps"}

r.hmset('who', d)

print(r.hgetall('who'))
