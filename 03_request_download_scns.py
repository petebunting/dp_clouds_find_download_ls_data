import usgs_m2m
import rsgislib.tools.utils
import rsgislib.tools.httptools
import random
import pprint
import glob
import tqdm
import os
import urllib.parse
import argparse

def request_download_scns(all_scns, out_dir):
    # Make sure the output directory exists if not create.
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    # Check whether any scenes have already been downloaded.
    scns = list()
    for scn in all_scns:
        scn_disp_id = scn["displayId"]
        out_file = os.path.join(out_dir, f"{scn_disp_id}.tar")
        if not os.path.exists(out_file):
            scns.append(scn)

    # Check the scenes are available for bulk download.
    scn_dsp_ids, scn_ent_ids = usgs_m2m.get_download_ids(scns, bulk=True)


    # Login
    # Define RSGIS_USGS_PASS
    api_key = usgs_m2m.usgs_login(username="petebunting", password=None)

    # Create the list of scenes on m2m
    n_scns = usgs_m2m.create_scene_list(api_key, dataset="landsat_ot_c2_l1", scn_ent_ids=scn_ent_ids, lst_name="dp_clouds_scns", lst_period="P1W")
    print("n_scns: {}".format(n_scns))

    # Get the list of downloads which are available
    dwlds_lst = usgs_m2m.check_dwnld_opts(api_key, lst_name="dp_clouds_scns", dataset="landsat_ot_c2_l1", dwnld_filetype="bundle", rm_lst=True )

    # Restrict the list of downloads to only the bundles ignoring the quicklook images.
    dwlds_bundle_lst = list()
    for dwnld in dwlds_lst:
        if dwnld["productId"] == "5e81f14f92acf9ef":
            dwlds_bundle_lst.append(dwnld)

    # Request the download URLs
    avail_dwn_urls, prep_dwnld_ids = usgs_m2m.request_downloads(api_key, dwlds_lst=dwlds_bundle_lst, dwnld_label="LS_Clouds_Test_Scns")

    print("avail_dwn_urls:")
    pprint.pprint(avail_dwn_urls)
    #print("prep_dwnld_ids:")
    #pprint.pprint(prep_dwnld_ids)

    # Iterate through URLs and download.
    for avail_scn in avail_dwn_urls:
        url_comps = urllib.parse.urlparse(avail_dwn_urls[avail_scn])
        scn_prod_id = str(url_comps.query.split("&")[0]).split("=")[1]
        out_file = os.path.join(out_dir, f"{scn_prod_id}.tar")
        print(f"Downloading: {out_file}")
        if not os.path.exists(out_file):
            rsgislib.tools.httptools.download_file_http(avail_dwn_urls[avail_scn], out_file)

    usgs_m2m.usgs_logout(api_key)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inscns", type=str, required=True, help="Scenes JSON file.")
    parser.add_argument("-o", "--outdir", type=str, required=True, help="Output directory.")
    args = parser.parse_args()

    """
    out_dir = "ls_downloads"

    scn_files = glob.glob("scn_dwnld_sets/*.json")
    all_scns = list()
    for scn_file in tqdm.tqdm(scn_files):
        scns_tmp = rsgislib.tools.utils.read_json_to_dict(scn_file)
        all_scns += scns_tmp
    """

    out_dir = args.outdir
    all_scns = rsgislib.tools.utils.read_json_to_dict(args.inscns)

    ##############################
    # Random subset for testing...
    #random.shuffle(all_scns)
    #all_scns = all_scns[0:5]
    ##############################

    print("Total number of scenes: {}".format(len(all_scns)))
    request_download_scns(all_scns, out_dir)
