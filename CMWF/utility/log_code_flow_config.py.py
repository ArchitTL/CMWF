# Databricks notebook source
# utility/log_code_flow_config.py
import logging
from variables.variables import log_code_flow_file_name

def setup_logger():
    logging.basicConfig(
        filename=log_code_flow_file_name,
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger()
