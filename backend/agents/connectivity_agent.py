class AttentionAgent:

```
def analyze_message(self, message):

    if "nodo" in message.lower():
        return {
            "intent": "diagnostic",
            "priority": "medium"
        }

    return {
        "intent": "unknown"
    }
```
