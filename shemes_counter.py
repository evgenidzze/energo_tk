import os

dir_path = 'media/schemes'


def row_counts():
    rows = 1
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
        if count == 4:
            rows += 1
            count = 1
    return rows