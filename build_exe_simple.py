#!/usr/bin/env python3
"""
Simple build script for MP4 to MP3 Converter
"""

import subprocess
import sys

# PyInstaller command for moviepy
# We need to include moviepy's ffmpeg binary
cmd = [
    "pyinstaller",
    "--onefile",
    "--console",
    "--name=MP4_to_MP3_Converter",
    "--clean",
    "src/skill_seekers/cli/mp4_to_mp3_converter.py"
]

print("Building MP4 to MP3 Converter...")
print("Command:", " ".join(cmd))
print("-" * 60)

try:
    subprocess.run(cmd, check=True)
    print("\n✓ Build successful!")
    print("\nExecutable location: dist\\MP4_to_MP3_Converter.exe")
except subprocess.CalledProcessError as e:
    print(f"\n✗ Build failed: {e}")
    sys.exit(1)
except FileNotFoundError:
    print("\n✗ PyInstaller not found. Install it with: pip install pyinstaller")
    sys.exit(1)
