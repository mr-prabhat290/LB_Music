import glob
import os

def __list_all_modules():
    plugin_path = os.path.dirname(os.path.abspath(__file__))

    mod_paths = glob.glob(f"{plugin_path}/**/*.py", recursive=True)

    all_modules = []
    for path in mod_paths:
        if path.endswith("__init__.py") or not path.endswith(".py"):
            continue
        module = (
            path.replace(plugin_path, "")
                .lstrip(os.sep)
                .replace(os.sep, ".")
                .replace(".py", "")
        )
        all_modules.append(module)

    return all_modules

ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
