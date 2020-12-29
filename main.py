import redis

try:
    conn = redis.StrictRedis(
        host='localhost',
        port=6379,
        db=0
    )
    print('Set Record: ', conn.set("test", "Hello World!"))
    print('Get Record: ', conn.get("test"))
    print('Delete Record: ', conn.delete("test"))
    print('Get Deleted Record: ', conn.get("test"))
except Exception as ex:
    print('Error', ex)