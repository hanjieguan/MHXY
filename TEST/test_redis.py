import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# r.lpush('test_list', 1)
# r.lpush('test_list', 2)
# r.lpush('test_list', 3)
# r.lpush('test_list', 4)
# r.lpush('test_list', 5)
# r.lpush('test_list', 6)
# r.lpush('test_list', 7)
# r.lpush('test_list',1,2,3,4,5,6,7,8)
# r.delete('test_list')
# r.ltrim('test_list', 0, 100)
# print(r.lrange('test_list', 0, -1))
# r.set('M1_time', 0)
# r.set('M2_time', 0)
# r.set('M3_time', 0)
# r.set('M1_time', 1)
# print(r.get('M1_time'))
# r.delete('S_M1')
print(r.lrange('test_list', 0, -1))
r.lrem('test_list', 0, 5)
print(r.lrange('test_list', 0, -1))
print(r.keys())