# -*- mode: python ; coding: utf-8 -*-

# PyInstaller 规格文件 - 修复版
# 包含imageio的元数据以解决 "PackageNotFoundError: No package metadata was found for imageio"

from PyInstaller.utils.hooks import copy_metadata

# 获取imageio和相关包的元数据
datas = []
datas += copy_metadata('imageio')
datas += copy_metadata('imageio-ffmpeg')
datas += copy_metadata('moviepy')
datas += copy_metadata('numpy')
datas += copy_metadata('Pillow')

a = Analysis(
    ['src/skill_seekers/cli/mp4_to_mp3_converter_gui_cn_fixed.py'],
    pathex=[],
    binaries=[],
    datas=datas,  # 包含元数据
    hiddenimports=[
        'moviepy',
        'moviepy.video',
        'moviepy.audio',
        'moviepy.video.io',
        'moviepy.audio.io',
        'moviepy.video.io.VideoFileClip',
        'moviepy.audio.io.AudioFileClip',
        'moviepy.config',
        'imageio',
        'imageio.plugins',
        'imageio.plugins.ffmpeg',
        'imageio_ffmpeg',
        'PIL',
        'PIL.Image',
        'numpy',
        'numpy.core',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter.test',
        'pytest',
        'matplotlib',
        'IPython',
        'sphinx',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MP4转MP3转换器_修复版',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

collect = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MP4转MP3转换器_修复版',
)
