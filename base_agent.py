
class Agent:
    def __init__(self):
        self.memory=None
    def act(self, obs):
        return {'action':'think','obs':obs}
