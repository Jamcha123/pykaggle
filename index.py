from kagglehub import dataset_download
import os
import argparse
import subprocess

def loading(author: str, dataset: str): 
    ans = author + "/" + dataset
    path = dataset_download(ans)


    if "public" in os.listdir(): 
        for x in os.listdir("public"): 
            os.remove("./public/" + str(x))
        os.rmdir("public")
    for x in os.listdir(path): 
        if x.split(".")[len(x.split("."))-1] != "csv": 
            continue
        
        targets = path + "/" + x
        print(targets)

        if "public" not in os.listdir(): 
            os.mkdir("public")

        f1 = open(targets, "r")
        data = str(f1.read())
        f1.close()

        f2 = open("./public/" + str(x), "w")
        f2.write(data)
        f2.close()

    return "kaggle dataset files created and stored in the public folder"
    
args = argparse.ArgumentParser(prog="pykaggle", description="pykaggle is a python cli tool to download kaggle datasets")
args.add_argument("-a", "--author", help="enter the author of the dataset in kaggle")
args.add_argument("-d", "--dataset", help="enter the dataset you want to download from kaggle (it has to be from the same author)")

parser = args.parse_args()
print(loading(parser.author, parser.dataset))
