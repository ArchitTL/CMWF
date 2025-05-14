# Databricks notebook source
# sourceCode/uc_mapping_config.py
from variables.variables import table_csv_path, old_new_ref_csv_path
from configs.configs_loader import build_uc_mapping_from_csvs

uc_mapping = build_uc_mapping_from_csvs(
    table_csv_path=table_csv_path,
    ref_csv_path=old_new_ref_csv_path
)
