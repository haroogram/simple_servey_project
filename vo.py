
class VOTE:
    
    def __init__(self, count: int=0):
        self.__count:int = count
    
    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, count):
        self.__count = count

class FOOD:
    
    def __init__(self, id: int, name: str | None = None, vote: VOTE | None = None):
        self.__id = id
        self.__name = name
        self.__vote: VOTE = vote
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def vote(self):
        return self.__vote

    @vote.setter
    def vote(self, vote):
        self.__vote = vote