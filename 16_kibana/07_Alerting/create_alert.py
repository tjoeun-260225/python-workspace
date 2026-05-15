# create_alert.py
import requests

ES = "http://localhost:9200"

watcher = {
    "trigger": {
        "schedule": {"interval": "1m"}
    },
    "input": {
        "search": {
            "request": {
                "indices": ["korea-cities"],
                "body": {
                    "query": {
                        "range": {"value": {"gt": 500}}
                    }
                }
            }
        }
    },
    "condition": {
        "compare": {
            "ctx.payload.hits.total.value": {"gt": 0}
        }
    },
    "actions": {
        "log_action": {
            "logging": {
                "text": "경보! value 500 초과 도시 감지: {{ctx.payload.hits.hits}}"
            }
        }
    }
}

res = requests.put(f"{ES}/_watcher/watch/high-value-alert", json=watcher)
print(res.json())