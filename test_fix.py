#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速修复imageio元数据问题的测试脚本
"""

try:
    # 尝试设置环境变量来避免检查版本
    import os
    os.environ["IMAGEIO_NO_INTERNET"] = "1"
    os.environ["IMAGEIO_USERDIR"] = os.path.expanduser("~").replace("\\", "/")

    # 尝试导入moviepy
    print("正在测试moviepy导入...")
    from moviepy import VideoFileClip
    print("✓ moviepy导入成功！")

    # 测试imageio
    import imageio
    print(f"✓ imageio版本: {imageio.__version__}")

    # 测试ffmpeg
    import imageio_ffmpeg
    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
    print(f"✓ ffmpeg路径: {ffmpeg_path}")

    print("\n所有依赖测试通过！程序应该可以正常运行。")

except Exception as e:
    print(f"✗ 测试失败: {e}")
    import traceback
    traceback.print_exc()
