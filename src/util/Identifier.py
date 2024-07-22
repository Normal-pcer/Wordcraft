class Identifier:
    namespace: str
    path: str

    def __init__(self, namespace: str, path: str):
        self.namespace = namespace
        self.path = path

    def __str__(self):
        return f"{self.namespace}:{self.path}"

    def __repr__(self):
        return f"{self.namespace}:{self.path}"

    def __eq__(self, other):
        return self.namespace == other.namespace and self.path == other.path

    def __hash__(self):
        return hash((self.namespace, self.path))
    
    @classmethod
    def from_str(cls, identifier_str: str):
        namespace, path = identifier_str.split(":")
        return cls(namespace, path)