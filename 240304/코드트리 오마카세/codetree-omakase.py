class Query:
    def __init__(self, cmd, t, x, name, n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n

queries = []

names = set()

p_queries = {}

position = {}

entry_time = {}
exit_time = {}

def cmp(q1, q2):
    if q1.t != q2.t:
        return q1.t < q2.t
    return q1.cmd < q2.cmd

L, Q = map(int, input().split())
for _ in range(Q):
    command = input().split()
    cmd, t, x, n = -1, -1, -1, -1
    name = ""
    cmd = int(command[0])
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
        position[name] = x

for name in names:
    exit_time[name] = 0
    for q in p_queries[name]:
        time_to_removed = 0
        if q.t < entry_time[name]:
            t_sushi_x = (q.x + (entry_time[name] - q.t)) % L
            additional_time = (position[name] - t_sushi_x + L) % L
            time_to_removed = entry_time[name] + additional_time
        else:
            additional_time = (position[name] - q.x + L) % L
            time_to_removed = q.t + additional_time
        
        exit_time[name] = max(exit_time[name], time_to_removed)
        queries.append(Query(111, time_to_removed, -1, name, -1))

for name in names:
    queries.append(Query(222, exit_time[name], -1, name, -1))

queries.sort(key= lambda q: (q.t, q.cmd))
people_num, sushi_num = 0, 0

for i in range(len(queries)):
    if queries[i].cmd == 100:
        sushi_num += 1
    elif queries[i].cmd == 111:
        sushi_num -= 1
    elif queries[i].cmd == 200:
        people_num += 1
    elif queries[i].cmd == 222:
        people_num -= 1
    else:
        print(people_num, sushi_num)