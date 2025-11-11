from dataclasses import dataclass

@dataclass
class VOTE:
    
    _count: int = 0
    
    # def __init__(self, count: int=0):
        # self.__count:int = count
    
    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, count):
        self._count = count

@dataclass
class FOOD:
    
    _id: int
    _name: str | None = None
    _vote: VOTE | None = None
    
    # def __init__(self, id: int, name: str | None = None, vote: VOTE | None = None):
    #     self.__id = id
    #     self.__name = name
    #     self.__vote: VOTE = vote
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def vote(self):
        return self._vote

    @vote.setter
    def vote(self, vote):
        self._vote = vote