
# Tracks when memory appears and how structure changes
def track(gen, agent):
    return {"generation":gen,"has_memory":agent.memory is not None}
