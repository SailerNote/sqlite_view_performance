import pickle


def save_variable(v, f):
    with open(f, 'wb') as f:
        pickle.dump(v, f)
    return f


def load_variable(f):
    with open(f, 'rb') as f:
        r = pickle.load(f)
    return r

