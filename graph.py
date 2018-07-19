class Vertex:
    def __init__(self, key):
        self.key = key
        self.connected_to = {}
        self.distance = 0
        self.predecessor = None
        self.color = 'white'

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

class Graph:
    def __init__(self):
        self.vert_dct = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dct.values())

    def __contains__(self, v):
        return v in self.vert_dct.keys()

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
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for v in g:
        for c in v.get_connections():
            #print(v.get_connections())
            print(f'{v.get_key()}, {c.get_key()}')
    for v in g:
        print(v)

    my_list = []
    for i in range(10):
        my_list.append(i)
    for i in range(10):
        print(my_list.pop())
    print(my_list)

main()


