"""
This type stub file was generated by pyright.
"""

import contextlib
import sys
from matplotlib import _docstring

"""
Core functions and attributes for the matplotlib style library:

``use``
    Select style sheet to override the current matplotlib settings.
``context``
    Context manager to use a style sheet temporarily.
``available``
    List available style sheets.
``library``
    A dictionary of style names and matplotlib settings.
"""
if sys.version_info >= (3, 10):
    ...
else:
    ...
_log = ...
__all__ = ['use', 'context', 'available', 'library', 'reload_library']
BASE_LIBRARY_PATH = ...
USER_LIBRARY_PATHS = ...
STYLE_EXTENSION = ...
STYLE_BLACKLIST = ...
_DEPRECATED_SEABORN_STYLES = ...
_DEPRECATED_SEABORN_MSG = ...
@_docstring.Substitution("\n".join(map("- {}".format, sorted(STYLE_BLACKLIST, key=str.lower))))
def use(style): # -> None:
    """
    Use Matplotlib style settings from a style specification.

    The style name of 'default' is reserved for reverting back to
    the default style settings.

    .. note::

       This updates the `.rcParams` with the settings from the style.
       `.rcParams` not defined in the style are kept.

    Parameters
    ----------
    style : str, dict, Path or list

        A style specification. Valid options are:

        str
            - One of the style names in `.style.available` (a builtin style or
              a style installed in the user library path).

            - A dotted name of the form "package.style_name"; in that case,
              "package" should be an importable Python package name, e.g. at
              ``/path/to/package/__init__.py``; the loaded style file is
              ``/path/to/package/style_name.mplstyle``.  (Style files in
              subpackages are likewise supported.)

            - The path or URL to a style file, which gets loaded by
              `.rc_params_from_file`.

        dict
            A mapping of key/value pairs for `matplotlib.rcParams`.

        Path
            The path to a style file, which gets loaded by
            `.rc_params_from_file`.

        list
            A list of style specifiers (str, Path or dict), which are applied
            from first to last in the list.

    Notes
    -----
    The following `.rcParams` are not related to style and will be ignored if
    found in a style specification:

    %s
    """
    ...

@contextlib.contextmanager
def context(style, after_reset=...): # -> Generator[None, Any, None]:
    """
    Context manager for using style settings temporarily.

    Parameters
    ----------
    style : str, dict, Path or list
        A style specification. Valid options are:

        str
            - One of the style names in `.style.available` (a builtin style or
              a style installed in the user library path).

            - A dotted name of the form "package.style_name"; in that case,
              "package" should be an importable Python package name, e.g. at
              ``/path/to/package/__init__.py``; the loaded style file is
              ``/path/to/package/style_name.mplstyle``.  (Style files in
              subpackages are likewise supported.)

            - The path or URL to a style file, which gets loaded by
              `.rc_params_from_file`.
        dict
            A mapping of key/value pairs for `matplotlib.rcParams`.

        Path
            The path to a style file, which gets loaded by
            `.rc_params_from_file`.

        list
            A list of style specifiers (str, Path or dict), which are applied
            from first to last in the list.

    after_reset : bool
        If True, apply style after resetting settings to their defaults;
        otherwise, apply style on top of the current settings.
    """
    ...

def update_user_library(library):
    """Update style library with user-defined rc files."""
    ...

def read_style_directory(style_dir): # -> dict[Unknown, Unknown]:
    """Return dictionary of styles defined in *style_dir*."""
    ...

def update_nested_dict(main_dict, new_dict):
    """
    Update nested dict (only level of nesting) with new values.

    Unlike `dict.update`, this assumes that the values of the parent dict are
    dicts (or dict-like), so you shouldn't replace the nested dict if it
    already exists. Instead you should update the sub-dict.
    """
    ...

class _StyleLibrary(dict):
    def __getitem__(self, key):
        ...
    


_base_library = ...
library = ...
available = ...
def reload_library(): # -> None:
    """Reload the style library."""
    ...

