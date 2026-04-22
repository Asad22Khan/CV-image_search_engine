import json
from pathlib import Path

json_path = Path("data/processed/coco-val-2017-500/metadata.json")

with open(json_path, 'r') as f:
    metadata = json.load(f)

for item in metadata:
    filename = Path(item["image_path"]).name 
    
    # ADDED data/raw/ right here 👇
    item["image_path"] = f"data/raw/coco-val-2017-500/{filename}"

with open(json_path, 'w') as f:
    json.dump(metadata, f, indent=4)

print("✅ Success! Paths updated.")