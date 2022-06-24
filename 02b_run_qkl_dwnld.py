import glob
import os
import rsgislib.tools.utils
import rsgislib.tools.httptools

out_dir = "qkl_imgs"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

#scn_files = glob.glob("scn_qlk_urls/*.json")
scn_files = ["scn_qlk_urls/43_13_cld_dp_scns_qkl_urls.json",
             "scn_qlk_urls/34_141_cld_dp_scns_qkl_urls.json",
             "scn_qlk_urls/23_204_cld_dp_scns_qkl_urls.json",
             "scn_qlk_urls/88_72_cld_dp_scns_qkl_urls.json",
             "scn_qlk_urls/80_110_cld_dp_scns_qkl_urls.json",
             "scn_qlk_urls/107_216_cld_dp_scns_qkl_urls.json",
             "scn_qlk_urls/57_189_cld_dp_scns_qkl_urls.json",
             "scn_qlk_urls/74_233_cld_dp_scns_qkl_urls.json"]

for scn_file in scn_files:
    scns = rsgislib.tools.utils.read_json_to_dict(scn_file)

    for scn in scns:
        scn_rowpath = scn.split("_")[2]
        print(scn_rowpath)
        scn_dir = os.path.join(out_dir, scn_rowpath)
        if not os.path.exists(scn_dir):
            os.mkdir(scn_dir)

        out_file = os.path.join(scn_dir, "{}.jpg".format(scn))
        if not os.path.exists(out_file):
            rsgislib.tools.httptools.download_file_http(scns[scn], out_file)
