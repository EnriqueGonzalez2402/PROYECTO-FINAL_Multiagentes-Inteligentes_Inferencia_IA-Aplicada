class InferenceAgent:

```
def evaluate(self, data):

    if data.get("tof", 0) > 100:
        return "Distancia excesiva"

    return "Sistema estable"
```
from fastapi import APIRouterS