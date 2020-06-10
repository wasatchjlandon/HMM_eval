import pandas as pd
#from pandas.io.json import json_normalize
import json
df = pd.read_json('/mnt/c/Users/willl/Downloads/all_metrics.json')

#df=pd.read_table('/mnt/c/Users/willl/Downloads/all_metrics.table')


#with open('/mnt/c/Users/willl/Downloads/20200603_metrics/190912_D00375_1913_BH3757BCX3_1.sample2vcf_rows.json') as json_data:
#    data = json.load(json_data)
#
#df = pd.json_normalize(data,'run_sample' ['INFO', 'rs2', ])
