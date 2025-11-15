# -*- coding: utf-8 -*-
"""
Hook for moviepy to ensure all submodules are included in PyInstaller bundle.
"""

from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Collect all moviepy submodules
hiddenimports = collect_submodules('moviepy')

# Collect data files (like ffmpeg binaries)
datas = collect_data_files('moviepy')

# Also include imageio which is used by moviepy
hiddenimports += collect_submodules('imageio')
datas += collect_data_files('imageio')

# Include numpy (required by moviepy)
hiddenimports += collect_submodules('numpy')

# Include decorator module (required by moviepy)
hiddenimports += collect_submodules('decorator')

# Include tqdm for progress bars
hiddenimports += collect_submodules('tqdm')
