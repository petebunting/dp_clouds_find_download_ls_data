import os
import tqdm
import random
import datetime
import geopandas
import usgs_m2m
import pprint
import rsgislib.tools.utils

out_dir = "scn_info"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

wrs2_gpdf = geopandas.read_file("ls_wrs2_land_areas_ran_smpl.gpkg", layer="ls_wrs2_land_areas_ran_smpl")

# Define RSGIS_USGS_PASS 
api_key = usgs_m2m.usgs_login(username="petebunting", password=None)

years = list(range(2013, 2023))
print(years)
cloud_thresholds = [25, 50, 75, 95]

for index, row in tqdm.tqdm(wrs2_gpdf.iterrows(), total=wrs2_gpdf.shape[0]):
    sel_scns = list()
    #print("[{}, {}]".format(row["PATH"], row["ROW"]))
    pt_lon, pt_lat = usgs_m2m.get_wrs_pt(api_key, row["ROW"], row["PATH"])
    scn_rowpath = "{}_{}".format(row["ROW"], row["PATH"])
    out_scn_file = os.path.join(out_dir, "{}_cld_dp_scns.json".format(scn_rowpath))
    
    if not os.path.exists(out_scn_file):
        for sel_year in years:        
            start_date = datetime.datetime(year=sel_year, month=1, day=1)
            end_date = datetime.datetime(year=sel_year, month=12, day=31)
            
            cloud_thres_low = 0
            for cloud_thres_up in cloud_thresholds:
                scns_lst = usgs_m2m.get_all_usgs_search(dataset="landsat_ot_c2_l1", api_key=api_key, max_n_rslts=90, start_date=start_date, end_date=end_date, cloud_min=cloud_thres_low, cloud_max=cloud_thres_up, pt=[pt_lat, pt_lon], full_meta=False)
                if len(scns_lst) > 0:
                    sel_scns.extend(random.choices(scns_lst, k=1))
                    
        
        rsgislib.tools.utils.write_dict_to_json(sel_scns, out_scn_file)
        
    
usgs_m2m.usgs_logout(api_key)

#for scn in sel_scns:
#    pprint.pprint(scn)




