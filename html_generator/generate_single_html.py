#!/usr/bin/python3

import sys
import integrate_res_in_html
import tinify_png
import os

workdir = os.getcwd()
projectRootPath = workdir + "/.."
resPath = projectRootPath + '/build/web-mobile/assets'

def generate_html(need2TinifyPic):
    if need2TinifyPic:
        print("=================== Start to Compress All Pictures ====================")
        tinify_png.tinifyPic(resPath)

    print("=================== Start to Integrate Res into Html ====================")
    integrate_res_in_html.integrate(projectRootPath)

if __name__ == '__main__':
    argc = len(sys.argv) - 1
    need2TinifyPic = False
    if argc > 0:
       arguments = sys.argv[1:] 
       need2TinifyPic = arguments[0]
    generate_html(need2TinifyPic)



