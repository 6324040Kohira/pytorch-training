from pathlib import Path

data dir = "04/example/data"
data_dir_path = Path(data_dir).resolve()
print("---absolute path---")

print("---all files under data_dir---")
file_list = list(data_dir.glob("*"))
for path in enumerate(file_list):
    print(path[1])