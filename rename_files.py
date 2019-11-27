import os

directory = r'C:\Users\hiral\OneDrive\Desktop\cal_pred\mm_dect\data\VOC2007\JPEGImages'

[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace('(', '_').replace(')','_')) for f in os.listdir(directory)]

# from tempfile import mkstemp
# from shutil import move
# from os import fdopen, remove
#
# def replace(file_path):
#     #Create temp file
#     fh, abs_path = mkstemp()
#     with fdopen(fh,'w') as new_file:
#         with open(file_path) as old_file:
#             for line in old_file:
#                 new_file.write(line.replace("(", "_").replace(")",'_'))
#     #Remove original file
#     remove(file_path)
#     #Move new file
#     move(abs_path, file_path)
#
# replace(r'C:\Users\hiral\OneDrive\Desktop\cal_pred\mm_dect\data\VOC2007\ImageSets\Main\val.txt')