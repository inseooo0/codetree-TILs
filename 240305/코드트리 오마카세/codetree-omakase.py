class Query:
    def __init__(self, cmd, t, x, name, n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n

entry_time = {}
exit_time = {}
positions = {}
names = set()
queries = []
p_queries = {}

L, Q = map(int, input().split())

for _ in range(Q):
    cmd, t, x, n = -1, -1, -1, -1
    name = ""
    command = input().split()
    cmd = int(command[0])

    #query generate
    if cmd == 100:
        t, x, name = command[1:]
        t, x = map(int, [t, x])
    elif cmd == 200:
        t, x, name, n = command[1:]
        t, x, n = map(int, [t, x, n])
    else:
        t = int(command[1])
    
    q = Query(cmd, t, x, name, n)
    queries.append(q)

    if cmd == 100:
        if name not in p_queries:
            p_queries[name] = []
        p_queries[name].append(q)
    elif cmd == 200:
        names.add(name)
        entry_time[name] = t
        positions[name] = x
    
for name in names:
    exit_time[name] = 0
    for q in p_queries[name]:
        if q.t < entry_time[name]:
            sushi_position = (q.x + (entry_time[name] - q.t)) % L
            remaining_time = (positions[name] - sushi_position + L) % L
            new_t = entry_time[name] + remaining_time
        else:
            remaining_time = (positions[name] - q.x + L) % L
            new_t = q.t + remaining_time

        queries.append(Query(201, new_t, -1, "", -1))
        exit_time[name] = max(exit_time[name], new_t)
    
    queries.append(Query(202, exit_time[name], -1, name, -1))

queries.sort(lambda k: (k.t, k.cmd))
num_sushi, num_people = 0, 0

for q in queries:
    if q.cmd == 100:
        num_sushi += 1
    elif q.cmd == 200:
        num_people += 1
    elif q.cmd == 201:
        num_sushi -= 1
    elif q.cmd == 202:
        num_people -= 1
    else:
        print(num_people, num_sushi)