
import random

def maybe_add_memory(agent):
    if agent.memory is None and random.random()<0.4:
        agent.memory={"episodic":[],"semantic":{}}
    return agent
