"""
file paths for all app files
"""

from pathlib import Path

import appdirs

from .__about__ import __name__ as name, __author__ as author

class AppDirs(appdirs.AppDirs):
    @property
    def files(self):
        return str(Path(self.site_data_dir, 'files'))

    @property
    def logs(self):
        return str(Path(self.site_data_dir, 'logs'))

    @property
    def plugins(self):
        return str(Path(self.site_data_dir, 'plugins'))

    # Use site dirs instead. Remap user dirs to prevent accidents
    @property
    def user_data_dir(self):
        return self.site_data_dir

    @property
    def user_config_dir(self):
        return self.site_config_dir


    @property
    def user_log_dir(self):
        return self.logs

    # Paths have been surpressed
    @property
    def user_cache_dir(self):
        pass

    @property
    def user_state_dir(self):
        pass

app_dirs = AppDirs(name, author)
