# -*- mode: python ; coding: utf-8 -*-

# PyInstaller 规格文件 - 用于打包MP4转MP3转换器中文版
# 使用方法: pyinstaller build_cn_gui.spec

block_cipher = None

# 定义要打包的主脚本
main_script = 'src/skill_seekers/cli/mp4_to_mp3_converter_gui_cn.py'

# 分析主脚本
a = Analysis(
    [main_script],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        # moviepy相关依赖
        'moviepy',
        'moviepy.video',
        'moviepy.audio',
        'moviepy.video.io',
        'moviepy.audio.io',
        'moviepy.editor',
        'moviepy.video.io.VideoFileClip',
        'moviepy.audio.io.AudioFileClip',
        'moviepy.decorators',
        'moviepy.tools',
        'imageio',
        'imageio.plugins',
        'imageio.plugins.ffmpeg',
        'imageio_ffmpeg',
        'PIL',
        'PIL.Image',
        'PIL.ImageDraw',
        'PIL.ImageFont',
        'numpy',
        'numpy.core.numeric',
        'proglog',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # 排除不必要的包以减小文件大小
        'tkinter.test',
        'numpy.random.tests',
        'numpy.testing',
        'matplotlib',
        'IPython',
        'sphinx',
        'pytest',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# 收集所有文件
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# 创建可执行文件
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MP4转MP3转换器',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 对于GUI应用，设置为False（不显示控制台窗口）
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[],  # 如果需要图标，可以添加.ico文件
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
    name='MP4转MP3转换器',
)
