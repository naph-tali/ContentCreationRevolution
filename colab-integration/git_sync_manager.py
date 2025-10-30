#!/usr/bin/env python3
"""
🔄 GIT SYNCHRONIZATION MANAGER
Automated git operations for Cosmic Projects
"""

import subprocess
import os
from datetime import datetime

class GitSyncManager:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def auto_commit(self, message=None):
        """Automatically commit changes with cosmic message"""
        if not message:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"cosmic: auto-sync {timestamp}"

        try:
            # Add all changes
            subprocess.run(["git", "-C", self.repo_path, "add", "."], check=True)

            # Commit
            subprocess.run(["git", "-C", self.repo_path, "commit", "-m", message], check=True)

            # Push
            subprocess.run(["git", "-C", self.repo_path, "push"], check=True)

            print(f"✅ Auto-commit: {message}")
            return True

        except subprocess.CalledProcessError as e:
            print(f"❌ Auto-commit failed: {e}")
            return False

    def get_sync_status(self):
        """Get synchronization status"""
        try:
            # Check if behind remote
            subprocess.run(["git", "-C", self.repo_path, "fetch"], check=True)

            status = subprocess.run(
                ["git", "-C", self.repo_path, "status", "-uno"],
                capture_output=True, text=True, check=True
            )

            if "Your branch is behind" in status.stdout:
                return "behind"
            elif "Your branch is up to date" in status.stdout:
                return "synced"
            else:
                return "unknown"

        except Exception as e:
            return f"error: {e}"

    def create_cosmic_tag(self, tag_name):
        """Create a cosmic version tag"""
        try:
            subprocess.run(
                ["git", "-C", self.repo_path, "tag", "-a", tag_name, "-m", "cosmic release"],
                check=True
            )
            subprocess.run(["git", "-C", self.repo_path, "push", "origin", tag_name], check=True)
            print(f"🎯 Cosmic tag created: {tag_name}")
            return True
        except Exception as e:
            print(f"❌ Tag creation failed: {e}")
            return False
