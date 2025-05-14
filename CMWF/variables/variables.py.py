# Databricks notebook source
# variables/variables.py

# --------------------------------------------
# Paths for local Databricks workspace
# --------------------------------------------
notebook_dir = "/Workspace/Repos/GizmoBox/GizmoboxProject"
log_migration_updates_file_path = "/dbfs/FileStore/tables/Archit/configs/logs/migration_log.jsonl"

# --------------------------------------------
# File Names and Extensions
# --------------------------------------------
log_code_flow_file_name = "/dbfs/FileStore/tables/Archit/configs/logs/code_debug.log"
log_migration_updates_file_name = "migration_log.jsonl"
inclusive_file_extensions = (".sql", ".py", ".ipynb", ".txt")

# --------------------------------------------
# Regex Patterns for legacy detection
# --------------------------------------------
patterns = {
    "hive_metastore": r"hive_metastore\\.\w+(?:\\.\w+)?",
    "adls_storage": r"abfss://[^\\s\"']+",
    "wasbs_storage": r"wasbs://[^\\s\"']+",
    "dbfs_storage": r"/dbfs/[^\\s\"']+"
}

# --------------------------------------------
# CSV Inputs for mapping
# --------------------------------------------
table_csv_path = "/dbfs/tfilestore/tables/Archit/configs/table_mappings.csv"
old_new_ref_csv_path = "/dbfs/FileStore/tables/Archit/configs/old__new_references.csv"

col_hive_db = "src_schema"
col_hive_table = "src_table"
col_uc_catalog = "catalog_name"
col_uc_db = "dst_schema"
col_uc_table = "dst_table"
col_old_path = "old"
col_new_path = "new"
