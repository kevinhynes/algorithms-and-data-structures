from time import sleep
wait = 2
class Vertex:
    def __init__(self, key):
        self.key = key
        self.connected_to = {}
        self.distance = 0
        self.predecessor = None
        self.color = 'white'
        self.discovery = 0
        self.finish = 0

    def __str__(self):
        return str(self.key) + ' is connected to ' + \
               str([f'{x.key} with weight {self.connected_to[x]}' \
                    for x in self.connected_to.keys()])

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_key(self):
        return self.key

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def set_distance(self, d):
        self.distance = d

    def get_distance(self):
        return self.distance

    def set_predecessor(self, p):
        self.predecessor = p

    def get_predecessor(self):
        return self.predecessor

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_discovery(self, time):
        self.discovery = time

    def set_finish(self, time):
        self.finish = time

class Graph:
    def __init__(self):
        self.vert_dct = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dct.values()) # Graph.vert_dct.values() == vertex objects

    def __contains__(self, v):
        return v in self.vert_dct.keys() # Graph.vert_dct.keys() == vertex keys (integers)

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_dct[key] = new_vertex
        self.num_vertices += 1
        return new_vertex

    def get_vertex(self, key):
        if key in self.vert_dct:
            return self.vert_dct[key]
        else:
            return None # Can't None be the default value?
                        # Would reduces this to "return vert_dct[key]"

    def get_vertices(self):
        return self.vert_dct.keys()

    def add_edge(self, fv, tv, weight=0):
        if fv not in self.vert_dct.keys():
            self.add_vertex(fv)
        if tv not in self.vert_dct.keys():
            self.add_vertex(tv)
        self.vert_dct[fv].add_neighbor(self.vert_dct[tv], weight)

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for v in self: # calls __iter__ to iterate thru vertices
            v.set_color('white')
            v.set_predecessor(-1) # Why isn't this a vertex object?
        for v in self:
            if v.get_color() == 'white':
                self.dfs_visit(v)

    def dfs_visit(self, start_vertex):
        start_vertex.set_color('gray')
        self.time += 1
        start_vertex.set_discovery(self.time)
        print(f'Starting at {start_vertex.key}')
        sleep(wait)
        print(f'{self.time}')
        sleep(wait)
        # vertex dictionary keys == vertex objects
        for next_vertex in start_vertex.get_connections():
            if next_vertex.color == 'white':
                print(f'Coming from {start_vertex.key}' + '\n' \
                      f'Visiting {next_vertex.key}')
                sleep(wait)
                next_vertex.set_predecessor(start_vertex)
                self.dfs_visit(next_vertex)
        
        start_vertex.set_color('black')
        self.time += 1
        print(f'Returning to {start_vertex.key}')
        sleep(wait)
        print(f'{self.time}')
        sleep(wait)
        start_vertex.set_finish(self.time)


def bfs(g, start):
    #start.set_distance(0)
    #start.set_predecessor(None)
    vertex_q = []
    vertex_q.insert(0, start)
    while len(vertex_q) > 0:
        cur_vertex = vertex_q.pop()
        for nbr in cur_vertex.get_connections():
            if nbr.get_color() == 'white':
                vertex_q.insert(0, nbr)
                nbr.set_color('gray')
                nbr.set_predecessor(cur_vertex)
                nbr.set_distance(cur_vertex.get_distance() + 1)
        cur_vertex.set_color('black')
    
def main():
    g = DFSGraph()
    for c in 'abcdef':
        g.add_vertex(c)

    g.add_edge('a', 'b')
    g.add_edge('a', 'd')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'b')
    g.add_edge('e', 'f')

    for v in g:
        for c in v.get_connections():
            print(f'{v.get_key()}, {c.get_key()}')
    for v in g:
        print(v)

    g.dfs()


main()


