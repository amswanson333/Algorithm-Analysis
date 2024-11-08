# A class to create an adjacency matrix object

class AdjacencyMatrix:
    
    def __init__(self, vertices: list, edges: list[tuple]):
        
        self.vertices = vertices
        self.edges = edges
        self.adjacency_matrix = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
        
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
            
            for (i, j, k) in self.edges:
                self.adjacency_matrix[i-1][j-1] = k
    
    def __repr__(self):
        return str(self.adjacency_matrix)
    
    def add_edge(self, start, end, weight: int = 1):
        
        # check if the start and end points exist in the graph
        if start in self.vertices:
            raise IndexError("Start Vertex does not exist.")
        if end in self.vertices:
            raise IndexError("End Vertex does not exist.")
        
        # check if an edge already exists
        if self.adjacency_matrix[start-1][end-1] != 0:
            raise ValueError("Edge already exists. Use edit_weight() to change the weight.")
        
        else:
            self.adjacency_matrix[start-1][end-1] = weight
            
    def edit_weight(self, start, end, weight: int):
        
        # check if the start and end points exist in the graph
        if start in self.vertices:
            raise IndexError("Start Vertex does not exist.")
        if end in self.vertices:
            raise IndexError("End Vertex does not exist.")
        
        # check if an edge exists
        if self.adjacency_matrix[start-1][end-1] == 0:
            raise ValueError("Edge does not exist. Use add_edge() to add the edge.")
            
        # check that weight is a valid value
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        elif weight == 0:
            raise ValueError("Weight cannot be zero. Use the delete_edge() method to delete the edge.")
        
        self.adjacency_matrix[start-1][end-1] = weight
    
    def delete_edge(self, start, end):
        
        # check if the start and end points exist in the graph
        if start in self.vertices:
            raise IndexError("Start Vertex does not exist.")
        if end in self.vertices:
            raise IndexError("End Vertex does not exist.")
        
        # check if an edge exists
        if self.adjacency_matrix[start-1][end-1] == 0:
            raise ValueError("Edge does not exist.")
        
        self.adjacency_matrix[start-1][end-1] = 0

    def add_vertex(self, vertex):
        
        # check vertex parameter
        if vertex in self.vertices:
            raise ValueError("Vertex already exists.")
        if type(vertex) is not int:
            raise ValueError("Vertex must be an integer.")
        if vertex != self.vertices[-1] + 1:
            print(f"Previous Vertex is {self.vertices[-1]}. Use {self.vertices[-1] + 1} instead.")
            raise ValueError("Vertex numbers must be consecutive.")
        
        # add the new vertex to the list of vertices
        self.vertices.append(vertex)
        
        # add a new row and column for the new vertex
        for l in self.adjacency_matrix:
            l.append(0)
        row = [0 for _ in range(len(self.vertices))]
        self.adjacency_matrix.append(row)
        
    def print_matrix(self):
        for row in self.adjacency_matrix:
            print(row)
        
    # todo: add a delete vertex method, need to determine how to handle vertex indices...