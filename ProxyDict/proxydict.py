class ProxyDict(object):
    def __init__(self, dictionnary) -> None:
        super().__init__()
        self.dictionnary = dictionnary

    def __getitem__(self, key):
        return self.dictionnary[key]

    def __setitem__(self, key, item):
        raise TypeError(f"{ProxyDict.__name__} object does not support item assignment")

    def __repr__(self):
        return f"{type(self).__name__}({self.dictionnary!r})"

    def __len__(self):
        return len(self.dictionnary)
        
    def __iter__(self):
        return iter(self.dictionnary)

    def __eq__(self, other):
        return self.dictionnary == other

    def items(self):
        return self.dictionnary.items()

    def values(self):
        return self.dictionnary.values()

    def get(self, key, default=None):
        return self.dictionnary.get(key, default)

    def keys(self):
        return self.dictionnary.keys()

if __name__ == "__main__":
    a = {"a" : 5, "b" : 6}
    b = {"c" : 4, "z" : 1}
    d = ProxyDict(a)
    e = ProxyDict(b)
    print(d.keys())
    print(d["a"])
    a["a"] = 10
    print(d["a"])
    print(len(d))
    print(d.items())
    print(d == e)