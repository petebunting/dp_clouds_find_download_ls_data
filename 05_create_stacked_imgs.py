#!/usr/bin/env python

import argparse
import atexit
import shutil
import tempfile

import create_ls_toa

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Creates Landsat TOA Stack from input .tar file"
    )
    parser.add_argument("intars", nargs="+", type=str, help="Input tar file(s)")
    parser.add_argument("-o", "--outdir", required=True, help="Output directory")
    args = parser.parse_args()

    tmp_dir = tempfile.mkdtemp(prefix="landsat_stack_tmp_")
    atexit.register(shutil.rmtree, tmp_dir, ignore_errors=True)

    for i, tar_file in enumerate(args.intars):
        print(f"[{i:03}/{len(args.intars):03}] {tar_file}")
        create_ls_toa.create_stacked_toa_ls_ols_cl2_lv1_img(
            tar_file, args.outdir, tmp_dir
        )

    shutil.rmtree(tmp_dir)
