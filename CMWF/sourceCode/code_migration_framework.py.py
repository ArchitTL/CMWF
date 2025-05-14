# Databricks notebook source
# code_migration_framework.py

import os
import re
import json
from datetime import datetime
from variables.variables import log_migration_updates_file_name, inclusive_file_extensions, patterns
from utility.log_code_flow_config import setup_logger

logger = setup_logger()

class CodeMigrationFramework:
    def __init__(self, notebook_dir=None, mapping=None, log_migration_updates_file_path=None):
        self.uc_mapping = mapping
        self.notebook_dir = notebook_dir
        self.log_migration_updates_file_path = log_migration_updates_file_path or os.path.join(notebook_dir, log_migration_updates_file_name)
        self.patterns = patterns
        os.makedirs(os.path.dirname(self.log_migration_updates_file_path), exist_ok=True)

    def scan_codebase(self):
        for root, _, files in os.walk(self.notebook_dir):
            for file in files:
                if file.endswith(inclusive_file_extensions):
                    path = os.path.join(root, file)
                    print(f"[{datetime.now()}] Scanning file: {path}")
                    logger.info(f"Scanning file: {path}")
                    with open(path, 'r') as f:
                        code = f.read()
                    self.identify_references(path, code)

    def identify_references(self, notebook_name, code):
        def detect_and_log(ref_type, match_text):
            old_ref = match_text
            new_ref = self.uc_mapping.get(old_ref, None)
            msg = f"[FOUND] {ref_type}: '{old_ref}' -> '{new_ref}' in {notebook_name}" if new_ref else f"[UNMAPPED] {ref_type}: '{old_ref}' in {notebook_name}"
            print(f"[{datetime.now()}] {msg}")
            logger.info(msg)
            self.log_findings(notebook_name, ref_type, old_ref, new_ref)

        for ref_type, pattern in self.patterns.items():
            for match in re.finditer(pattern, code):
                detect_and_log(ref_type, match.group(0))

        sql_magic_blocks = re.findall(r"# MAGIC %sql\s+(.*?)(?=(# MAGIC|$))", code, re.DOTALL)
        for sql_block, _ in sql_magic_blocks:
            for ref_type, pattern in self.patterns.items():
                for match in re.finditer(pattern, sql_block):
                    detect_and_log(ref_type, match.group(0))

    def log_findings(self, notebook, ref_type, old_value, new_value):
        log_entry = {
            "notebook": notebook,
            "ref_type": ref_type,
            "old_value": old_value,
            "new_value": new_value,
            "detected_at": datetime.now().isoformat()
        }
        with open(self.log_migration_updates_file_path, 'a') as log_file:
            log_file.write(json.dumps(log_entry) + '\n')

    def replace_references(self):
        for root, _, files in os.walk(self.notebook_dir):
            for file in files:
                if file.endswith(inclusive_file_extensions):
                    path = os.path.join(root, file)
                    print(f"[{datetime.now()}] Replacing references in {path}")
                    logger.info(f"Replacing references in {path}")
                    with open(path, 'r', encoding='utf-8') as f:
                        code = f.read()
                    for old, new in self.uc_mapping.items():
                        code = code.replace(old, new)
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(code)
