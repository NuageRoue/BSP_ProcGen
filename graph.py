class GrapheDico:
    def __init__(self):
        self.adj = {}

    def addRoom(self,s):
        if s not in self.adj:
            self.adj[s] = set()
    
    def addAdj(self,s1,s2):
        self.addRoom(s1)
        self.addRoom(s2)
        self.adj[s1].add(s2)
        self.adj[s2].add(s1)

    def arc(self, s1, s2) :
        return s2 in self.adj[s1]

    def getRoomList(self):
        return list(self.adj)

    def getNeighborOf(self, s):
        return list(self.adj[s])

    def nbNeighborOf(self, s):
        return len(self.getNeighborOf(s))

    def nbRoom(self):
        return len(self.adj)

def graphGen(roomList):
    graph = GrapheDico()
    for room in roomList:
        #graph.addSommet(room)
        for roomAdj in room.adj:
            graph.addAdj(room, room.adj[roomAdj])
    return graph