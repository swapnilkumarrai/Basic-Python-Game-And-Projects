import os


folder = r"C:\\swapnil\\clearing_clutter"
extensions={}
totalfiles = 0
totalfolders = 0

for root, dirs, files in os.walk(folder):
    totalfolders += len(dirs)
    totalfiles += len(files)
    for file in files:
        name, ext = os.path.splitext(file)
        if ext in extensions:
            extensions[ext] += 1
        else:
            extensions[ext] = 1

print('Total number of files:', totalfiles)
print('Total number of folders:', totalfolders)
print('Total:', (totalfolders + totalfiles))
print("\nFile extensions and their count:")
for key, value in extensions.items():
    print(f"{key}: {value}")
