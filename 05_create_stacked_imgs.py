import glob
import create_ls_toa

out_dir = "/Users/pete/Temp/dp_cloud_masking/process_landsat/out"
tmp_dir = "/Users/pete/Temp/dp_cloud_masking/process_landsat/tmp"

tar_files = glob.glob("/Users/pete/Temp/dp_cloud_masking/process_landsat/ls_downloads/*.tar")
for tar_file in tar_files:
    create_ls_toa.create_stacked_toa_ls_ols_cl2_lv1_img(tar_file, out_dir, tmp_dir)

