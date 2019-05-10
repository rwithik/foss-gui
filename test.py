import pickle

d = {'website': {'user': 'pass'}}

f = open("entries", "wb")
pickle.dump(d, f)
f.close()