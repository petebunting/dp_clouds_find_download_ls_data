import os
import glob
import math
import tqdm
import rsgislib.tools.utils

n_scns_blk = 500

out_dir = "scn_dwnld_sets"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

scn_files = glob.glob("scn_info/*.json")
all_scns = list()
for scn_file in tqdm.tqdm(scn_files):
    scns_tmp = rsgislib.tools.utils.read_json_to_dict(scn_file)
    all_scns += scns_tmp

n_scns = len(all_scns)
print(f"Total number of scenes: {n_scns}")
n_full_blks = math.floor(n_scns / n_scns_blk)
rem_scns = n_scns - (n_scns_blk * n_full_blks)

print(f"{n_full_blks} blocks with {rem_scns} scns remaining")

scn_n_s = 0
for n in range(n_full_blks):
    scn_n_e = scn_n_s + n_scns_blk
    print(f"{scn_n_s}:{scn_n_e}")
    scns_sub = all_scns[scn_n_s:scn_n_e]
    out_file = os.path.join(out_dir, f"scns_set_{n}.json")
    rsgislib.tools.utils.write_dict_to_json(scns_sub, out_file)
    scn_n_s += n_scns_blk

scn_n_e = scn_n_s + rem_scns
print(f"{scn_n_s}:{scn_n_e}")
scns_sub = all_scns[scn_n_s:scn_n_e]
out_file = os.path.join(out_dir, f"scns_set_{n_full_blks}.json")
rsgislib.tools.utils.write_dict_to_json(scns_sub, out_file)
