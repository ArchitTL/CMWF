# Databricks notebook source
# configs/configs_loader.py
import pandas as pd
from variables.variables import col_hive_db, col_hive_table, col_uc_catalog, col_uc_db, col_uc_table, col_old_path, col_new_path

def build_uc_mapping_from_csvs(table_csv_path: str, ref_csv_path: str) -> dict:
    mapping = {}

    table_df = pd.read_csv(table_csv_path, encoding="utf-8-sig")
    table_df.columns = table_df.columns.str.strip()

    for _, row in table_df.iterrows():
        hive_fqn = f"hive_metastore.{row[col_hive_db]}.{row[col_hive_table]}"
        uc_fqn = f"{row[col_uc_catalog]}.{row[col_uc_db]}.{row[col_uc_table]}"
        mapping[hive_fqn] = uc_fqn

    ref_df = pd.read_csv(ref_csv_path)
    ref_df.columns = ref_df.columns.str.strip()

    for _, row in ref_df.iterrows():
        mapping[row[col_old_path]] = row[col_new_path]

    return mapping
