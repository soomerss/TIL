import pickle

name = "hi"
age = 12341

with open("pik.p", "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)


with open("pik.p", "rb") as file:
    dd = pickle.load(file)
    ff = pickle.load(file)

    print(dd)
    print(ff)
