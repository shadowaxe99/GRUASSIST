
"""
documentation.py
This module is responsible for generating the documentation of the project.
"""

import os
import inspect
from pydoc import html

def generate_documentation(module):
    """
    Generate HTML documentation for a module.
    """
    doc = html.page(inspect.getdoc(module), inspect.getsource(module))
    with open(f"{module.__name__}.html", "w") as f:
        f.write(doc)

if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import main
    generate_documentation(main)
