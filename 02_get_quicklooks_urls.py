import rsgislib.tools.utils


scns = rsgislib.tools.utils.read_json_to_dict("cloud_testing_scns.json")


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

rsgislib.tools.utils.write_dict_to_json(scn_qkl_paths, "cloud_testing_scns_qkl_paths.json")
        
