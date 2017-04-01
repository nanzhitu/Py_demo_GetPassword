#encoding=utf-8
import ConfigParser
import re

def Config_read(config_ini):
    config = ConfigParser.ConfigParser()
    config_file = open(config_ini)
    try:
        config.readfp(config_file)
    finally:
        config_file.close()
    return config

def Config_write(config_ini,config):
    config_file = open(config_ini,'w')
    try:
        config.write(config_file)
    finally:
        config_file.close()
