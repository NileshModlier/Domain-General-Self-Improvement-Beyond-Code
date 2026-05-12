
class Semantic:
    def update(self, memory, key, value):
        memory['semantic'][key]=value
        return memory
