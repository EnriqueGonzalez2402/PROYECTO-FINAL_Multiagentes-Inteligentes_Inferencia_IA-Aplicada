# test_connectivity.py

from backend.agents.connectivity_agent import ConnectivityAgent

agent = ConnectivityAgent()

result = agent.verify_nodes(3)

print(result)