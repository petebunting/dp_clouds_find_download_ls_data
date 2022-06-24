import rsgislib.tools.filetools
import rsgislib.tools.utils
import glob
import os

out_dir = "scn_qlk_urls"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

scn_files = glob.glob("scn_info/*.json")

for scn_file in scn_files:
    basename = rsgislib.tools.filetools.get_file_basename(scn_file)
    scns = rsgislib.tools.utils.read_json_to_dict(scn_file)

    out_file = os.path.join(out_dir, "{}_qkl_urls.json".format(basename))
    scn_qkl_paths = dict()
    for scn in scns:
        found = False
        for browser_scn in scn["browse"]:
            if browser_scn["browseName"] == "Reflective Browse":
                scn_browse_path = browser_scn["browsePath"]
                found = True
                break
        if found:
            scn_qkl_paths[scn["displayId"]] = scn_browse_path

    rsgislib.tools.utils.write_dict_to_json(scn_qkl_paths, out_file)

