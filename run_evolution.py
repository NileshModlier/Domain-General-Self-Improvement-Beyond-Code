
from agent.base_agent import Agent
from agent.mutators import maybe_add_memory
from analysis.timeline import track
import json

agent=Agent()
records=[]
for gen in range(30):
    agent=maybe_add_memory(agent)
    records.append(track(gen,agent))
with open('results/memory_timeline.json','w') as f:
    json.dump(records,f,indent=2)
print('Memory evolution complete.')
