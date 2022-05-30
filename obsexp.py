import os
import pathlib
import shutil
import re

res_dir_name = "_res"
source_res_dir = "/home/ec/win_d/sync/vaults/homemain/_res"
source_dir = "/home/ec/win_d/sync/vaults/homemain/040_tech 💻/infosec"
dest_dir = "/home/ec/win_d/temp/infosec"

dest_path = shutil.copytree(source_dir, dest_dir)

with open("/home/ec/win_d/res_file.txt", 'w+') as rf:
   for dir_name, sub_dir_list, file_list in os.walk(dest_path):
      for sub_dir in sub_dir_list:
         sub_dir_res_path = os.path.join(dir_name, os.path.join(sub_dir, res_dir_name))
         if os.path.isdir(sub_dir_res_path):
            sub_dir_list.remove(sub_dir)
      
      if len(file_list) > 0: #if we have files....
         cur_res_path = os.path.join(dir_name, res_dir_name)

         os.mkdir(cur_res_path)

         for file_name in file_list:
            md_file = os.path.join(dir_name, file_name)

            #search each file for all image references
            if os.path.isfile(md_file) and pathlib.PurePath(md_file).suffix == '.md':
               rf.write(md_file + '\n')

               with open(md_file, 'r') as md_f:
                  md_text = md_f.read()
      
               for file_resource in re.compile(r"_res\/(.*)\)").finditer(md_text):
                  rf.write(os.path.join(source_res_dir, file_resource.group(1)) + " --> " + cur_res_path + '\n')
                  shutil.copy(os.path.join(source_res_dir, file_resource.group(1)), cur_res_path)

               with open(md_file, 'w+') as md_f:
                  md_f.write(md_text.replace("../",""))
      
      
      