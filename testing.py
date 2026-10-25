import numpy as np

def cosine_simil(a,b):
    dotproduct = np.dot(a,b)
    alength = np.linalg.norm(a)
    blength = np.linalg.norm(b)
    magnitude = alength*blength
    if magnitude == 0:
        return 0
    simil = dotproduct / magnitude
    return simil
def search(db,query,k):
    maxcos = 0
    maxcoslist = []
    maxname = []
    for name,vector in db.items():
        similarity = cosine_simil(vector,query)
        if similarity > maxcos:
            maxcos = similarity
            maxcoslist.append(similarity)
            maxname.append(name)
    if k > len(db) or k<0:
        print("k is out of bounds")
        return
    kreturnname = maxname[-k:]
    kreturnvec = maxcoslist[-k:]
    return kreturnname,kreturnvec

helloworld =[1,1]
hello =[1,0]
print(cosine_simil(helloworld,hello))
namedict = {"Eessa": [1,1],"Jamie":[1,2],"Subhan":[2,2],"Zakki":[2,1]}
print(search(namedict,[2,1],2))