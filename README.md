# example-fractal-task-arguments

[Fractal](https://fractal-analytics-platform.github.io/) is a framework developed at the [BioVisionCenter](https://www.biovisioncenter.uzh.ch/en.html) to process bioimaging data at scale in the OME-Zarr format and prepare the images for interactive visualization. Find more information about Fractal in general and the other repositories at the [Fractal home page](https://fractal-analytics-platform.github.io).


This repository includes a mock package of Fractal tasks, which is meant to used as a test/example case in:
1. The [`fractal-task-tools`](https://github.com/fractal-analytics-platform/fractal-task-tools) feature for generating the task-package manifest and the JSON schemas for arguments of each specific task.
2. The [`fractal-web`](https://github.com/fractal-analytics-platform/fractal-web) feature that generates UI components based on a task-arguments JSON schema, see sandboxes at https://fractal-analytics-platform.github.io/fractal-web/sandbox-pages.

## How to use

1. Prepare a virtual environments and install the project:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```
2. Generate the manifest via `fractal-manifest create --package example-tasks` and find the generated manifest file at `src/example_tasks/__FRACTAL_MANIFEST__.json`. This file can be uploaded to https://fractal-analytics-platform.github.io/fractal-web/sandbox/#task-manifest, to review how [`fractal-web`](https://github.com/fractal-analytics-platform/fractal-web) would render the user interface to edit task arguments.
3. Make a change in the call signature of a task (e.g. in `src/example_tasks/task1.py`) and re-generate the manifest. Then review how it would be rendered.
4. Extract single-task JSON schema from the manifest via `./single_json_schemas/extract.py`, which generates JSON schema files in the `single_json_schemas/` folder. Then review the corresponding `fractal-web` user-interface at https://fractal-analytics-platform.github.io/fractal-web/sandbox/#jschema, where you can also interactively edit the JSON Schema until you reach the expected result.
