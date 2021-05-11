import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "src",
    "given_data"
    "models"
]

for dir in dirs:
    os.mkdirs(dir, exist_ok == True)
    with open(os.path.join(dir, ".gitkeep"), w) as f:
        pass

