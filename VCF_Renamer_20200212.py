import pandas as pd
import shutil
import os

fc_id = "H755TBCX3"
original_path = "C:\\Users\\jlandon\\Downloads\\val_feas_20_HMM_part1\\" + fc_id + "\\"
#^^^^^^^modify the lines above each run
file_list = os.listdir(original_path)
#list_trimmed_filenames = [name[4:] for name in list_ori_filenames]
list_mod_filenames = [(fc_id + "_" + name[4:]) for name in file_list]
os.mkdir(original_path[:-1] + "_2\\")
destination_path = original_path[:-1] + "_2\\"

for i in file_list:
    x = file_list.index(i)
    shutil.copyfile((original_path + i), (destination_path + list_mod_filenames[x]))
    print((destination_path + list_mod_filenames[x]) + " HAS BEEN WRITTEN!")
