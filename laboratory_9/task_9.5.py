class Disconnect(Exception):
    pass


def connect_user(x):
    with open('user'+' ' + x + '.txt', 'w') as file:
        yield from write_to_file(file)


def write_to_file(f_obj):
    while True:
        try:
            x = yield
            f_obj.write(x + '\n')
        except Disconnect:
            yield

def user_connection(username):
    import random
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"

def establish_connection(auth=True):
    import random
    id = f"{random.randint(0,100000000):010}"
    if auth:
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"


def connection():
    import random
    connections = [establish_connection(True) for i in range(2)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))

    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]


open_users = dict()
for i in connection():
    if 'auth' in i:
        user_id=i[5:]
        open_users[user_id] = connect_user(user_id)
        next(open_users[user_id])
    elif 'message' in i and i[:10] in open_users:
        user_id=i[:10]
        message=i[11:]
        open_users[user_id].send(message)
    elif 'disconnect' in i:
        user_id = i[11:]
        open_users[user_id].throw(Disconnect)