import rsgislib.dataaccess.usgs_m2m
import rsgislib.tools.utils
import random
import pprint


scns = rsgislib.tools.utils.read_gz_json_to_dict("cloud_testing_scns.json.gz")
# Subset for testing...
random.shuffle(scns)
scns = scns[:5]

pprint.pprint(scns[0])

#scn_dsp_ids, scn_ent_ids = rsgislib.dataaccess.usgs_m2m.get_download_ids(scns, bulk=True)

#pprint.pprint(scn_dsp_ids)

"""
# Define RSGIS_USGS_PASS 
api_key = rsgislib.dataaccess.usgs_m2m.usgs_login(username="petebunting", password=None)

n_scns = rsgislib.dataaccess.usgs_m2m.create_scene_list(api_key, dataset="landsat_ot_c2_l1", scn_ent_ids=scn_ent_ids, lst_name="dp_clouds_scns", lst_period="P1W")

dwlds_lst = rsgislib.dataaccess.usgs_m2m.check_dwnld_opts(api_key, lst_name="dp_clouds_scns", dataset="landsat_ot_c2_l1", dwnld_filetype="bundle", rm_lst=False)

avail_dwn_urls, prep_dwnld_ids = rsgislib.dataaccess.usgs_m2m.request_downloads(api_key, dwlds_lst="dp_clouds_scns", dwnld_label="LS Clouds Test Scns")

rsgislib.dataaccess.usgs_m2m.usgs_logout(api_key)
"""