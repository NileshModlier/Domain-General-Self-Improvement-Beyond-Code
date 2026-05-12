
class Episodic:
    def store(self, memory, event):
        memory['episodic'].append(event)
        return memory
