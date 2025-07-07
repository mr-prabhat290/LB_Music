import glob
import os

def __list_all_modules():
    # Get absolute path of the current folder (plugins/)
    plugin_path = os.path.dirname(os.path.abspath(__file__))

    # Collect all Python files in subfolders and root
    mod_paths = glob.glob(f"{plugin_path}/**/*.py", recursive=True)

    all_modules = [
        (
            f.replace(plugin_path, "")
             .replace(os.sep, ".")
             .lstrip(".")
             .replace(".py", "")
        )
        for f in mod_paths
        if f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return all_modules

ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
