# Metadata Editing Plugin

An example plugin that sets or updates custom sample-level metadata.

## Installation

```shellx
fiftyone plugins download https://github.com/allenleetc/edit_metadata_example
```

Refer to the [main README](https://github.com/voxel51/fiftyone-plugins) for
more information about managing downloaded plugins and developing plugins
locally.

## Usage

[Install fiftyone](https://docs.voxel51.com/getting_started/install.html#fiftyone-installation)
and then run the following code to load a quickstart dataset. If you have previously used fiftyone, you can load an existing dataset instead.

```py
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset('quickstart')

session = fo.launch_app(dataset,auto=False)
```

2. Select some samples in the sample grid.

3.  Run the `Edit Custom Metadata` operator to set or update some metadata fields! 
