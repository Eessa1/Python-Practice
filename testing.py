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
    valuesdict = {}
    for name,vector in db.items():
        similarity = cosine_simil(vector,query)
        valuesdict[name] = similarity
    if k > len(db) or k<0:
        print("k is out of bounds")
        return
    highestkvalues = dict(sorted(valuesdict.items(), key=lambda item: item[1], reverse= True)[:k])
    return highestkvalues

helloworld =[1,1]
hello =[1,0]
##print(cosine_simil(helloworld,hello))
namedict = {"Eessa": [1,1],"Jamie":[1,2],"Subhan":[2,2],"Zakki":[2,1]}
print(search(namedict,[2,1],2))