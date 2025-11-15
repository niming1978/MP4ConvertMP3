# -*- mode: python ; coding: utf-8 -*-

# PyInstaller 规格文件 - 用于打包MP4转MP3转换器中文版
# 使用方法: pyinstaller build_final.spec


a = Analysis(
    ['src/skill_seekers/cli/mp4_to_mp3_converter_gui_cn.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        # moviepy完整导入
        'moviepy',
        'moviepy.video',
        'moviepy.audio',
        'moviepy.video.io',
        'moviepy.audio.io',
        'moviepy.editor',
        'moviepy.video.fx',
        'moviepy.audio.fx',
        'moviepy.video.io.VideoFileClip',
        'moviepy.audio.io.AudioFileClip',
        'moviepy.decorators',
        'moviepy.tools',
        'moviepy.utils',
        'moviepy.config',
        'moviepy.audio.AudioClip',
        'moviepy.audio.io.ffmpeg_audiowriter',
        'moviepy.video.VideoClip',
        'moviepy.video.compositing.CompositeVideoClip',
        # imageio和ffmpeg
        'imageio',
        'imageio.plugins',
        'imageio.plugins.ffmpeg',
        'imageio_ffmpeg',
        'imageio_ffmpeg._utils',
        'imageio_ffmpeg._io',
        # PIL/Pillow
        'PIL',
        'PIL.Image',
        'PIL.ImageDraw',
        'PIL.ImageFont',
        'PIL._imaging',
        # numpy
        'numpy',
        'numpy.core',
        'numpy.core.numeric',
        'numpy.linalg',
        'numpy.fft',
        # 其他moviepy依赖
        'proglog',
        'tqdm',
        'requests',
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
        'numpy.testing',
        'numpy.random.tests',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# 收集所有文件
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# 创建可执行文件（GUI版本，无控制台窗口）
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
    console=False,  # GUI应用程序不显示控制台
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# 收集所有依赖
collect = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='MP4转MP3转换器',
)