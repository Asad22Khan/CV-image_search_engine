import json
from pathlib import Path

def ensure_processed_dir(raw_path):
    raw_path = Path(raw_path)
    # "c:/abc/def/image_01000" --> raw_path.name --> image_01000
    processed_path = raw_path.parent.parent / "processed" / raw_path.name
    processed_path.mkdir(parents=True, exist_ok=True)
    return processed_path


def save_metadata(metadata, raw_path):
    processed_path = ensure_processed_dir(raw_path)

    output_path = processed_path / "metadata.json"
    with open(output_path, 'w') as f:
        json.dump(metadata, f)
    return output_path

def load_metadata(metadata_path=None):
    """
    Loads metadata either from a custom path or the default production path.
    """
    from pathlib import Path
    import json
    
    # If no path is provided (Test Mode), use the default secure path
    if metadata_path is None:
        file_path = Path("data") / "processed" / "coco-val-2017-500" /"metadata.json"
    else:
        # If a path IS provided (Developer Mode), use that one
        file_path = Path(metadata_path)
    
    if file_path.exists() and file_path.is_file():
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        raise FileNotFoundError(f"Could not find metadata at {file_path.absolute()}")
        

def get_unique_classes_counts(metadata):
    unique_classes = set()
    count_options = {}

    for item in metadata:
        for cls in item['detections']:
            unique_classes.add(cls['class'])
            if cls['class'] not in count_options:
                count_options[cls['class']]= set()
            count_options[cls['class']].add(cls['count'])

    unique_classes = sorted(unique_classes)
    for cls in count_options:
        count_options[cls] = sorted(count_options[cls])
    
    return unique_classes, count_options

