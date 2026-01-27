from pathlib import Path
import json

manifest_path = Path(__file__).parents[1] / "src/example_tasks/__FRACTAL_MANIFEST__.json"
data_dir = Path(__file__).parent
with manifest_path.open("r") as f:
    manifest = json.load(f)
print(f"Manifest loaded from {str(manifest_path)}")
for item in manifest["task_list"]:
    task_name = item["name"]
    args_schema_parallel = item.get("args_schema_parallel")
    args_schema_non_parallel = item.get("args_schema_non_parallel")
    if args_schema_non_parallel is not None:
        with (data_dir / f"{task_name}-non-parallel.json").open("w") as f:
            json.dump(args_schema_non_parallel, f, indent=2)
    if args_schema_parallel is not None:
        with (data_dir / f"{task_name}-parallel.json").open("w") as f:
            json.dump(args_schema_parallel, f, indent=2)