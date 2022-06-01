import os
import pathlib
import shutil
import re

res_dir_name = "_res"
source_res_dir = "/home/ec/win_d/sync/vaults/homemain/_res"
source_dir = "/home/ec/win_d/sync/vaults/homemain/040_tech 💻/infosec"
dest_dir = "/home/ec/win_d/temp/infosec"

dest_path = shutil.copytree(source_dir, dest_dir)

for dir_name, sub_dir_list, file_list in os.walk(dest_path):

   #if a folder contains the resource folder we can skip that folder and it's subs
   #because it's already as wanted: _res folder local
   for sub_dir in sub_dir_list:
      sub_dir_res_path = os.path.join(dir_name, os.path.join(sub_dir, res_dir_name))
      if os.path.isdir(sub_dir_res_path):
         sub_dir_list.remove(sub_dir)
   
   #if we have files in the current folder, then we need a resource folder
   if len(file_list) > 0: #if we have files....
      cur_res_path = os.path.join(dir_name, res_dir_name)

      #...create the new resource folder
      os.mkdir(cur_res_path)

      #fore each file in this folder, we need to fetch the resources from the old 
      #folder and move it to the new, local folder
      for file_name in file_list:
         cur_file = os.path.join(dir_name, file_name)

         #...if it's an MD file
         if os.path.isfile(cur_file) and pathlib.PurePath(cur_file).suffix == '.md':
            with open(cur_file, 'r') as md_f:
               md_text = md_f.read()
   
            #use regex, for each resource, copy it from the old folder
            #use the first group (file name) from the regex search
            for file_resource in re.compile(r"_res\/(.*)\)").finditer(md_text):
               shutil.copy(os.path.join(source_res_dir, file_resource.group(1)), cur_res_path)

            #remove the '../' form the links in the MD files, not needed anymore
            #as the resource folder _res is local
            with open(cur_file, 'w+') as md_f:
               md_f.write(md_text.replace("../",""))  