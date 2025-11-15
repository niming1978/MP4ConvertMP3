#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MP4转MP3转换器打包脚本
将中文版程序打包为独立的exe文件
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path


def check_and_install_requirements():
    """检查并安装所需的依赖包"""
    print("="*60)
    print("检查依赖包...")
    print("="*60)
    print()

    required_packages = [
        "PyInstaller",
        "moviepy",
        "imageio-ffmpeg"
    ]

    for package in required_packages:
        try:
            __import__(package.lower().replace('-', '_'))
            print(f"✓ {package} 已安装")
        except ImportError:
            print(f"  正在安装 {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✓ {package} 安装完成")

    print()


def clean_build_dirs():
    """清理旧的构建文件"""
    print("清理旧的构建文件...")

    dirs_to_clean = ["build", "dist"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"  已删除: {dir_name}")

    print()


def get_ffmpeg_path():
    """获取imageio_ffmpeg的ffmpeg路径"""
    try:
        import imageio_ffmpeg
        ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
        return ffmpeg_path
    except:
        # 尝试常见的安装位置
        possible_paths = [
            os.path.join(sys.prefix, "Lib", "site-packages", "imageio_ffmpeg", "binaries", "ffmpeg-win64-v4.2.2.exe"),
            os.path.join(sys.prefix, "Lib", "site-packages", "imageio_ffmpeg", "binaries", "ffmpeg.exe"),
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None


def build_gui_version():
    """打包GUI版本"""
    print("="*60)
    print("打包GUI版本（图形界面）...")
    print("="*60)
    print()

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name", "MP4转MP3转换器",
        "--noconfirm",
        "--clean",
        "--onefile",
        "--windowed",
        "--hidden-import", "moviepy",
        "--hidden-import", "moviepy.video",
        "--hidden-import", "moviepy.audio",
        "--hidden-import", "moviepy.video.io",
        "--hidden-import", "moviepy.audio.io",
        "--hidden-import", "imageio",
        "--hidden-import", "imageio_ffmpeg",
        "--hidden-import", "PIL",
        "--hidden-import", "PIL.Image",
        "--hidden-import", "numpy",
        "--hidden-import", "numpy.core.numeric",
        "--exclude-module", "matplotlib",
        "--exclude-module", "pytest",
        "--exclude-module", "IPython",
        "src/skill_seekers/cli/mp4_to_mp3_converter_gui_cn.py"
    ]

    print("执行命令:")
    print(" ".join(cmd))
    print()

    result = subprocess.run(cmd)

    if result.returncode != 0:
        print()
        print("错误：打包GUI版本失败！")
        return False

    print()
    print("✓ GUI版本打包完成")
    print()
    return True


def build_cli_version():
    """打包命令行版本"""
    print("="*60)
    print("打包命令行版本...")
    print("="*60)
    print()

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name", "MP4转MP3转换器_CMD",
        "--noconfirm",
        "--clean",
        "--onefile",
        "--console",
        "--hidden-import", "moviepy",
        "--hidden-import", "moviepy.video",
        "--hidden-import", "moviepy.audio",
        "--hidden-import", "moviepy.video.io",
        "--hidden-import", "moviepy.audio.io",
        "--hidden-import", "imageio",
        "--hidden-import", "imageio_ffmpeg",
        "--hidden-import", "PIL",
        "--hidden-import", "numpy",
        "--exclude-module", "tkinter",
        "--exclude-module", "matplotlib",
        "--exclude-module", "pytest",
        "--exclude-module", "IPython",
        "src/skill_seekers/cli/mp4_to_mp3_converter_cn.py"
    ]

    print("执行命令:")
    print(" ".join(cmd))
    print()

    result = subprocess.run(cmd)

    if result.returncode != 0:
        print()
        print("错误：打包命令行版本失败！")
        return False

    print()
    print("✓ 命令行版本打包完成")
    print()
    return True


def show_result():
    """显示打包结果"""
    print("="*60)
    print("打包完成！")
    print("="*60)
    print()

    # 检查生成的文件
    dist_dir = Path("dist")

    if dist_dir.exists():
        print("生成的文件：")
        print()

        gui_exe = dist_dir / "MP4转MP3转换器.exe"
        if gui_exe.exists():
            size = gui_exe.stat().st_size / (1024 * 1024)
            print(f"  ✓ GUI版本（双击运行）:")
            print(f"    - 路径: {gui_exe}")
            print(f"    - 大小: {size:.1f} MB")
            print(f"    - 用法: 双击运行即可启动图形界面")
            print()

        cli_exe = dist_dir / "MP4转MP3转换器_CMD.exe"
        if cli_exe.exists():
            size = cli_exe.stat().st_size / (1024 * 1024)
            print(f"  ✓ 命令行版本:")
            print(f"    - 路径: {cli_exe}")
            print(f"    - 大小: {size:.1f} MB")
            print(f"    - 用法: 在命令提示符中运行")
            print(f"      示例: MP4转MP3转换器_CMD.exe video.mp4 audio.mp3")
            print()

    print("="*60)
    print("重要提示：")
    print("  - 首次运行程序可能需要解压依赖，请耐心等待")
    print("  - 程序会自行解压ffmpeg等组件到临时目录")
    print("  - 无需安装Python或其他任何软件")
    print("  - 可在任何Windows 10/11电脑上直接运行")
    print("="*60)
    print()

    # 尝试打开输出目录
    try:
        if sys.platform == "win32":
            os.startfile(dist_dir)
        else:
            print(f"输出目录: {dist_dir.absolute()}")
    except:
        pass


def main():
    """主函数"""
    print()
    print("="*60)
    print("MP4转MP3转换器 - 打包工具")
    print("="*60)
    print()

    # 检查依赖
    check_and_install_requirements()

    # 清理旧的构建文件
    clean_build_dirs()

    # 打包GUI版本
    success = build_gui_version()

    if success:
        # 打包命令行版本
        success = build_cli_version()

    if success:
        # 显示结果
        show_result()
        print("程序打包成功！✓")
    else:
        print()
        print("打包过程中出现错误。请检查上面的输出信息。")
        sys.exit(1)


if __name__ == "__main__":
    main()
