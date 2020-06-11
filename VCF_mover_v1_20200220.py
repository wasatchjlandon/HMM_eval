import pandas as pd
import shutil
import os

moving_list = "C:\\Users\\jlandon\\Downloads\\VCFExport_prod_1-24-19\\All_renamed_norm_vcf_files\\moving_list.csv"
source_path = "C:\\Users\\jlandon\\Downloads\\VCFExport_prod_1-24-19\\All_renamed_norm_vcf_files\\"
dest_path = "C:\\Users\\jlandon\\Downloads\\VCFExport_prod_1-24-19\\Study_Samples_renamed_norm_vcf\\"
#^^^^^^^modify the lines above each run
file = pd.read_csv(moving_list, header=None, names=["ori_file"])
df_mv_l = pd.DataFrame(file)
list_ori_filenames = [name for name in df_mv_l.ori_file]
#list_trimmed_filenames = [name[4:] for name in list_ori_filenames]
#list_mod_filenames = [(fc_id + "_" + name) for name in list_ori_filenames]
#os.mkdir(original_path[:-1] + "_2\\")
#destination_path = original_path[:-1] + "_2\\"

for i in list_ori_filenames:
#    x = list_ori_filenames.index(i)
    shutil.copyfile((source_path + i + ".norm.vcf"), (dest_path + i + ".called.vcf"))
    print(dest_path + i + " HAS BEEN WRITTEN!")
