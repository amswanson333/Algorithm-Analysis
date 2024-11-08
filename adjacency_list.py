# adjacency table class

class AdjacencyList:
    
    def __init__(self, vertices: list, edges: list[tuple]):
        
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = dict.fromkeys(self.vertices,[])  # type: dict[int, list[tuple]]
        
        # if a list of edges is provided, loop through the edges and add to the matrix
        if self.edges:
            # handle error cases if the edge list is not the correct format
            for i, t in enumerate(self.edges):
                if type(t) is not tuple:
                    # edges must be tuples
                    raise TypeError("Edges list includes invalid entries. The provided list must only contain tuples.")
                elif len(t) < 2:
                    # edges must have two vertices
                    raise ValueError("Edges list tuples must include a start and stop Vertex.")
                elif t[0] not in self.vertices or t[1] not in self.vertices:
                    # vertices must exist in the vertex list
                    raise ValueError("First two entries in each Edge tuple must be a Vertex.")
                elif len(t) == 2:
                    # format the edges to include weights if they were excluded
                    self.edges[i] = t + (1,)
                elif len(t) >= 3:
                    # edge weights cannot be 0 or negative values
                    if t[2] <= 0:
                        raise ValueError("Third entry in the Edge tuple cannot be less than or equal to 0. Use 1 for unweighted Edges.")
                    # edge tuples cannot have more than 3 entries
                    if len(t) > 3:
                        raise ValueError("Too many entries in the Edge tuple. Use only two or three.")
                    
            # compose the list from the vertices
            for k in self.adjacency_list:
                for t in self.edges:
                    if t[0] == k:
                        temp_list = [(t[1], t[2])]
                        self.adjacency_list[k] = self.adjacency_list[k] + temp_list

    def __repr__(self):
        return str(self.adjacency_list)
    
    def add_edge(self, start, end, weight: int = 1):
        # todo
        pass
    
    def edit_weight(self, start, end, weight: int):
        # todo
        pass
    
    def delete_edge(self, start, end):
        # todo
        pass
    
    def add_vertex(self, vertex):
        #todo
        pass
    
    def print_list(self):
        print("Start \t -> \t (End, Weight)")
        for k in self.adjacency_list:
            print(f"{k} \t -> \t {self.adjacency_list[k]}")