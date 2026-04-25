import os
import pkgutil

__version__ = "2.4.0"

_inner = os.path.join(os.path.dirname(__file__), __name__)
if os.path.isdir(_inner):
    __path__ = pkgutil.extend_path(__path__, __name__)
    if _inner not in __path__:
        __path__.append(_inner)
