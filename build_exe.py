#!/usr/bin/env python3
"""
Build script for MP4 to MP3 Converter

This script builds the MP4 to MP3 converter into a standalone Windows executable
using PyInstaller.
"""

import os
import sys
import subprocess
from pathlib import Path


def build_executable():
    """Build the MP4 to MP3 converter as a standalone executable."""

    # Get the project root directory
    project_root = Path(__file__).parent

    # Path to the main script
    main_script = project_root / "src" / "skill_seekers" / "cli" / "mp4_to_mp3_converter.py"

    # Check if the main script exists
    if not main_script.exists():
        print(f"Error: Main script not found at {main_script}")
        sys.exit(1)

    print("Building MP4 to MP3 Converter executable...")
    print(f"Project root: {project_root}")
    print(f"Main script: {main_script}")
    print("-" * 60)

    # PyInstaller command arguments
    pyinstaller_args = [
        "pyinstaller",
        "--onefile",  # Create a single executable file
        "--windowed",  # No console window (optional, remove if you want console)
        "--name=MP4_to_MP3_Converter",  # Name of the executable
        "--distpath=dist",  # Output directory
        "--workpath=build",  # Build temporary directory
        "--specpath=.",  # Directory for spec file
        "--clean",  # Clean cache before building
        "--add-binary=venv/Lib/site-packages/moviepy/videoio/ffmpeg;moviepy/videoio/ffmpeg",  # Include ffmpeg
        str(main_script),  # Input script
    ]

    # Alternative: You can also use a spec file for more complex configurations
    print("Running PyInstaller...")
    print(" ".join(pyinstaller_args))
    print("-" * 60)

    try:
        # Run PyInstaller
        result = subprocess.run(pyinstaller_args, cwd=str(project_root), capture_output=False)

        if result.returncode == 0:
            print("\n" + "=" * 60)
            print("✓ Build successful!")
            exe_path = project_root / "dist" / "MP4_to_MP3_Converter.exe"
            print(f"\nExecutable created at: {exe_path}")
            print("=" * 60)

            # Verify the executable was created
            if exe_path.exists():
                file_size = exe_path.stat().st_size / (1024 * 1024)  # MB
                print(f"File size: {file_size:.2f} MB")
                return True
            else:
                print("Warning: Executable file not found in expected location")
                return False
        else:
            print(f"\n✗ Build failed with return code: {result.returncode}")
            return False

    except FileNotFoundError:
        print("Error: PyInstaller not found. Please install it with:")
        print("  pip install pyinstaller")
        sys.exit(1)
    except Exception as e:
        print(f"Error during build: {e}")
        sys.exit(1)


def build_with_spec():
    """Alternative build method using a spec file."""

    spec_content = '''
# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules
import sys
sys.setrecursionlimit(5000)

# Collect all moviepy submodules
hiddenimports = collect_submodules('moviepy')

a = Analysis(
    ['src/skill_seekers/cli/mp4_to_mp3_converter.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MP4_to_MP3_Converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
'''

    spec_file = Path("MP4_to_MP3_Converter.spec")
    with open(spec_file, "w") as f:
        f.write(spec_content)

    print(f"Created spec file: {spec_file}")
    print("Running PyInstaller with spec file...")

    try:
        result = subprocess.run(["pyinstaller", str(spec_file)], capture_output=False)
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    """Main function."""
    print("MP4 to MP3 Converter - Build Script")
    print("=" * 60)

    # Check if running on Windows
    if sys.platform != "win32":
        print("Warning: This build script is designed for Windows.")
        print(f"Current platform: {sys.platform}")

    # Build the executable
    success = build_executable()

    if success:
        print("\nBuild completed successfully!")
        print("\nYou can find the executable in: .\\dist\\MP4_to_MP3_Converter.exe")
        print("\nUsage examples:")
        print("  MP4_to_MP3_Converter.exe video.mp4 audio.mp3")
        print("  MP4_to_MP3_Converter.exe --batch ./videos ./mp3s")
    else:
        print("\nBuild failed. Check the output above for errors.")
        sys.exit(1)


if __name__ == "__main__":
    main()
