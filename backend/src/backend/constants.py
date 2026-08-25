"""
Store reusable path constants for the application.

Keeping paths here avoids repeating path-building logic in other files.
"""

from pathlib import Path


# __file__ represents the location of this constants.py file.
#
# Path(__file__) converts that location into a pathlib Path object.
#
# parents[2] moves two directory levels above the directory that
# contains constants.py.
#
# / "data" then adds the data folder to the resulting project path.
#
# Example project structure:
#
# project/
# ├── data/
# │   └── Pokemon.csv
# └── src/
#     └── backend/
#         └── constants.py
#
# In this example, DATA_PATH points to:
# project/data
DATA_PATH = Path(__file__).parents[2] / "data"