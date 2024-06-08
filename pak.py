import json
import sys
import os
import zipfile

OUT_PUT_PATH = "/mnt/f/work/"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ("python pak.py llama3 latest output_path")
        exit(0)
    if len(sys.argv) > 3:
        OUT_PUT_PATH = sys.argv[3]
    
    lib_name = sys.argv[1]
    lib_version = sys.argv[2]
    tar_filelist = []
    json_path = f"_data/models/manifests/registry.ollama.ai/library/{lib_name}/{lib_version}"
    
    if os.path.exists(json_path):

        tar_filelist.append(json_path)
        # print(f"add {json_path} to tar_filelist")
        
        fp = open(json_path, "r")
        json_dict = json.load(fp)
        print (json_dict)

        tar_filelist.append(os.path.join("_data/models/blobs", json_dict['config']['digest'].replace(":","-")))
        tar_filelist.append(os.path.join("_data/models/blobs", json_dict['layers'][0]['digest'].replace(":","-")))
        tar_filelist.append(os.path.join("_data/models/blobs", json_dict['layers'][1]['digest'].replace(":","-")))
        tar_filelist.append(os.path.join("_data/models/blobs", json_dict['layers'][2]['digest'].replace(":","-")))
        tar_filelist.append(os.path.join("_data/models/blobs", json_dict['layers'][3]['digest'].replace(":","-")))

        print (tar_filelist)

        print ("start zip file")
        zip_file = zipfile.ZipFile(f'{OUT_PUT_PATH}{lib_name}_{lib_version}.zip','w')
        for filename in tar_filelist:
            print (f"add {filename}")
            zip_file.write(filename,compress_type=zipfile.ZIP_DEFLATED)
        zip_file.close()
        print ("zip over")