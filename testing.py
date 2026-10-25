import numpy as np

def cosine_simil(a,b):
    dotproduct = np.dot(a,b)
    alength = np.linalg.norm(a)
    blength = np.linalg.norm(b)
    magnitude = alength*blength
    if magnitude == 0:
        return "0 divison"
    simil = dotproduct / magnitude
    return simil

helloworld =[1,1]
hello =[1,0]
print(cosine_simil(helloworld,hello))