import os
import pathlib

for dir_name, sub_dir_list, file_list in os.walk("/home/ec/win_d/sync/vaults/homemain/040_tech 💻/infosec"):
   print(dir_name)
   print(pathlib.PurePath(dir_name).name)
   for file_name in file_list:
      print(file_name)

