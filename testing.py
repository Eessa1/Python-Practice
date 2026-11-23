import numpy as np

class VectorDB:
    def __init__(self):
        self.vectors = {}

    def add(self,name,vector):
        self.vectors[name] = vector

    def search(self,query,k):
        if k<0 or k >len(self.vectors):
            raise ValueError("k is out of bounds")

        scores = {}
        for name,vector in self.vectors.items():
            scores[name] = cosine_simil(vector,query)

        ranked = sorted(scores.items(),key = lambda item: item[1], reverse = True)
        return dict(ranked[:k])

def cosine_simil(a,b):
    dotproduct = np.dot(a,b)
    alength = np.linalg.norm(a)
    blength = np.linalg.norm(b)
    magnitude = alength*blength
    if magnitude == 0:
        return 0
    simil = dotproduct / magnitude
    return simil

db = VectorDB()
db.add("Eessa", [1,1])
db.add("Jamie", [1,2])
db.add("Subhan", [2,2])
db.add("Zakki", [2,1])
print(db.search([2,1],2))
