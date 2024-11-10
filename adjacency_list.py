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
        
        # check if start and stop exist
        if start not in self.vertices:
            raise IndexError("Start vertex does not exist.")
        if end not in self.vertices:
            raise IndexError("End vertex does not exist.")
        
        # check if an edge already exists
        for t in self.adjacency_list[start]:
            if t[0] == end:
                raise ValueError("Edge already exists, use edit_weight() to change the edge weight.")
        
        # check that weight is a valid value
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        elif weight == 0:
            raise ValueError("Weight cannot be zero. Use the delete_edge() method to delete the edge.")
        
        # add the edge to the appropriate start vertex
        self.adjacency_list[start] = self.adjacency_list[start] + [(end, weight)]
        # todo: add print output to confirm addition
            
    def edit_weight(self, start, end, weight: int):
        
        # check if start and stop exist
        if start not in self.vertices:
            raise IndexError("Start vertex does not exist.")
        if end not in self.vertices:
            raise IndexError("End vertex does not exist.")
        
        # check if an edge exists
        for i,t in enumerate(self.adjacency_list[start]):
            if t[0] == end:
                # save the index of the tuple for later
                edge_index = i
                break
            if i == len(self.adjacency_list[start]) - 1:
                raise ValueError("Edge does not exist. Use the add_edge() method to add an edge with a specific weight.")
        
        # check that weight is a valid value
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        elif weight == 0:
            raise ValueError("Weight cannot be zero. Use the delete_edge() method to delete the edge.")

        self.adjacency_list[start][edge_index] = (end,weight)
        # todo: add print output to confirm change
    
    def delete_edge(self, start, end):
        
        # check if start and stop exist
        if start not in self.vertices:
            raise IndexError("Start vertex does not exist.")
        if end not in self.vertices:
            raise IndexError("End vertex does not exist.")
        
        # check if an edge exists
        for i,t in enumerate(self.adjacency_list[start]):
            if t[0] == end:
                # save the index of the tuple for later
                edge_index = i
                break
            if i == len(self.adjacency_list[start]) - 1:
                raise ValueError("Edge does not exist. Nothing to delete.")
            
        self.adjacency_list[start].pop(edge_index)
        # todo: add print output to confirm change
    
    def add_vertex(self, vertex):

        # check vertex parameter
        if vertex in self.vertices:
            raise ValueError("Vertex already exists.")
        if type(vertex) is not int:
            raise ValueError("Vertex must be an integer.")
        if vertex != self.vertices[-1] + 1:
            print(f"Previous Vertex is {self.vertices[-1]}. Use {self.vertices[-1] + 1} instead.")
            raise ValueError("Vertex numbers must be consecutive.")
        
        self.adjacency_list[vertex] = []
    
    def print_list(self):
        print("Start \t -> \t (End, Weight)")
        for k in self.adjacency_list:
            print(f"{k} \t -> \t {self.adjacency_list[k]}")