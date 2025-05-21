import json
from datetime import datetime

data = {
    "last_updated": datetime.utcnow().isoformat() + "Z",
    "message": "This file was updated by GitHub Actions!"
}

with open("status.json", "w") as f:
    json.dump(data, f, indent=2)

print("status.json updated.")
