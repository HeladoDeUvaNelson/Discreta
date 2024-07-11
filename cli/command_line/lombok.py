def Getter(cls):
    obj = cls
    
    methods = [a for a in dir(obj) if not a.startswith('__') and callable(getattr(obj, a))]
    attrs = [a for a in dir(obj) if not a.startswith('__') and not callable(getattr(obj, a))]

    def createObjectMethod(name = str) -> str:
        old_name = name
        if name[0] == '_': name = name[1:]
        name = "get_" + name
        
        if name in methods: return None

        def get(self):
            return self.__getattribute__(old_name)

        setattr(cls, name, get)
        
    [createObjectMethod(attr) for attr in attrs]
    
    return cls

def Setter(cls):
    obj = cls
    
    methods = [a for a in dir(obj) if not a.startswith('__') and callable(getattr(obj, a))]
    attrs = [a for a in dir(obj) if not a.startswith('__') and not callable(getattr(obj, a))]
    
    def createObjectMethod(name = str) -> str:
        old_name = name
        if name[0] == '_': name = name[1:]
        name = "set_" + name

        if name in methods: return None
        
        def set(self, val):
            self.__setattr__(old_name, val)

        setattr(cls, name, set)
        
    [createObjectMethod(attr) for attr in attrs]
    
    return cls