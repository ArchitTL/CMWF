# Databricks notebook source
# databricks_run_migration.py

import sys
sys.path.append("/Workspace/Users/archit.murgudkar@tlconsulting.com.au/CMWF")

from variables.variables import notebook_dir, log_migration_updates_file_path
from configs.configs_loader import build_uc_mapping_from_csvs
from sourceCode.uc_mapping_config import uc_mapping
from sourceCode.code_migration_framework import CodeMigrationFramework
from utility.log_code_flow_config import setup_logger

logger = setup_logger()

framework = CodeMigrationFramework(
    notebook_dir=notebook_dir,
    mapping=uc_mapping,
    log_migration_updates_file_path=log_migration_updates_file_path
)

framework.scan_codebase()
framework.replace_references()

msg = "Migration Completed..."
print(msg)
logger.info(msg)
