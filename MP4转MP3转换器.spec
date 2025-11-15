# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\skill_seekers\\cli\\mp4_to_mp3_converter_gui_cn.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['moviepy', 'moviepy.video', 'moviepy.video.io.VideoFileClip', 'moviepy.audio.io.AudioFileClip', 'imageio', 'imageio_ffmpeg', 'PIL', 'numpy'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MP4转MP3转换器',
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
