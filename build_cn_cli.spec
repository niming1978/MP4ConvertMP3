# -*- mode: python ; coding: utf-8 -*-

# PyInstaller 规格文件 - 用于打包MP4转MP3转换器（命令行版本）
# 使用方法: pyinstaller build_cn_cli.spec

block_cipher = None

# 定义要打包的主脚本
main_script = 'src/skill_seekers/cli/mp4_to_mp3_converter_cn.py'

# 分析主脚本
a = Analysis(
    [main_script],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'moviepy',
        'moviepy.video',
        'moviepy.audio',
        'moviepy.video.io',
        'moviepy.audio.io',
        'moviepy.editor',
        'moviepy.video.io.VideoFileClip',
        'moviepy.audio.io.AudioFileClip',
        'imageio',
        'imageio.plugins',
        'imageio.plugins.ffmpeg',
        'imageio_ffmpeg',
        'PIL',
        'PIL.Image',
        'numpy',
        'numpy.core.numeric',
        'proglog',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'tkinter.test',
        'matplotlib',
        'IPython',
        'sphinx',
        'pytest',
        'numpy.random.tests',
        'numpy.testing',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# 收集所有文件
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# 创建可执行文件（命令行版本显示控制台）
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MP4转MP3转换器_CMD',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 命令行版本显示控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[],
)

# 收集所有依赖
collect = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MP4转MP3转换器_CMD',
)
