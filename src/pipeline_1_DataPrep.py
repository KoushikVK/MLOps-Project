import os
import argparse
import yaml
import logging



def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)  #loads yaml file and return it 

    return config


def main(config_path,datasource):
    config = read_params(config_path)  #to read all contents from yaml file


    

if __name__ =="__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.find("config","params.yaml") #While running in different environmnets the file will be in differenet directories(fr other OS , in order to counter this problem we use this)
    
    args.add_argument("--config",default = default_config_path) #adding all the files from config directory 
    args.add_argument("--datasource",default = None)#Adding training data batch here
    parsed_args = args.parse_args()#parsing added argumnets
    main(config_path = parsed_args.config,datasource = parsed_args.datasource) #main function will be called here
