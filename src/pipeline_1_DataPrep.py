import os
import argparse
import yaml
import logging



if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default = None) #adding all the files from config directory 
    args.add_argument("--datasource",default = None)#Adding training data batch here
    parsed_args = args.parse_args()#parsing added argumnets
    print(parsed_args.config,parsed_args.datasource)
    