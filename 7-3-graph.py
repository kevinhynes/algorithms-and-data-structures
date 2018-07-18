class Vertex:
    def __init__(self, key):
        self.key = key
        self.connected_to = {}

    def __str__(self):
        return str(self.id) + ' is connected to ' + str([x.id for x in self.connected_to])

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_key(self):
        return self.key

    def get_weight(self, nbr):
        return self.connected_to[nbr]

class Graph:
    def __init__(self):
        self.vert_dct = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dct.values())

    def __contains__(self, v):
        return v in self.vert_dct

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_dct[key] = new_vertex
        self.num_vertices += 1
        return new_vertex

    def get_vertex(self, key):
        if key in vert_dct:
            return vert_dct[key]
        else:
            return None # Can't None be the default value?
                        # Would reduces this to "return vert_dct[key]"

    def get_vertices(self):
        return self.vert_dct.keys()

    def add_edge(self, fv, tv, weight=0):
        if fv not in self.vert_dct:
            self.add_vertex(fv)
        if tv not in self.vert_dct:
            self.add_vertex(tv)
        self.vert_dct[fv].add_neighbor(self.vert_dct[tv], weight)

    

    

