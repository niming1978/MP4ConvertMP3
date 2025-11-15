# MP4 to MP3 Converter - GUI Version Guide

## Overview

The GUI version provides an intuitive graphical interface for converting MP4 video files to MP3 audio files. No command line knowledge required!

## Features

- **Single File Conversion**: Convert individual MP4 files to MP3
- **Batch Conversion**: Convert all MP4 files in a directory at once
- **Progress Tracking**: Real-time progress bar and status messages
- **Detailed Logging**: View conversion logs in real-time
- **Auto-naming**: Automatically generates output filenames
- **Error Handling**: Comprehensive error messages and recovery

## Installation

No installation required! Just download the executable file and run it.

### Prerequisites
- Windows operating system
- No Python or other dependencies needed (everything is bundled)

## Quick Start

1. **Download the executable**: `MP4_to_MP3_Converter_GUI.exe`
2. **Double-click to run**: No installation needed
3. **Start converting**: Select files or directories and click "Convert"

## Usage Guide

### Single File Conversion

1. **Select mode**: Choose "Single File" mode
2. **Select input file**: Click "Browse..." next to "Input MP4 File" and select your video file
3. **Select output file** (optional): Click "Browse..." next to "Output MP3 File" to choose where to save the converted file
   - If not specified, the output will be saved in the same location as the input with the same name but .mp3 extension
4. **Click "Convert"**: The conversion will start immediately
5. **Wait for completion**: Watch the progress bar and status messages
6. **View results**: Check the output location for your converted MP3 file

### Batch Conversion (Directory)

1. **Select mode**: Choose "Batch (Directory)" mode
2. **Select input directory**: Click "Browse..." next to "Input Directory" and select the folder containing your MP4 files
3. **Select output directory**: Click "Browse..." next to "Output Directory" to choose where to save all converted MP3 files
4. **Click "Convert"**: All MP4 files in the input directory will be converted
5. **Monitor progress**: View the progress bar and log messages for each file
6. **View results**: All MP3 files will be saved in the output directory

## Interface Overview

```
┌─────────────────────────────────────────────────┐
│        MP4 to MP3 Converter                     │
├─────────────────────────────────────────────────┤
│  Conversion Mode:                               │
│  ○ Single File  ○ Batch (Directory)            │
├─────────────────────────────────────────────────┤
│  Input MP4 File:                                │
│  [__________________________________] [Browse..]│
│                                                  │
│  Output MP3 File (optional):                    │
│  [__________________________________] [Browse..]│
├─────────────────────────────────────────────────┤
│  Status: Ready                                  │
│  [===============   ] 60%                       │
├─────────────────────────────────────────────────┤
│  Log:                                            │
│  • Converting: video.mp4                        │
│  ✓ Successfully converted: audio.mp3            │
│  • Status: Complete!                            │
├─────────────────────────────────────────────────┤
│  [Convert]  [Clear Log]  [Exit]                 │
└─────────────────────────────────────────────────┘
```

## Button Functions

- **Convert**: Start the conversion process
- **Clear Log**: Clear the log window
- **Exit**: Close the application (will warn if conversion is in progress)

## Log Messages

The log area displays real-time messages:

- **• [info]**: Informational messages (gray)
- **✓ [success]**: Successful operations (green)
- **✗ [error]**: Error messages (red)
- **⚠ [warning]**: Warning messages (orange)

**Example log output:**
```
• Loading video file...
• Converting: video.mp4 -> audio.mp3
✓ Successfully converted: audio.mp3
• Status: Complete!
```

## Tips and Best Practices

### For Single Files
- You can select any video format that MoviePy supports (MP4, AVI, MKV, MOV, etc.)
- If you don't specify an output file, the MP3 will be saved in the same directory as the input
- The filename will be the same as the input, just with .mp3 extension

### For Batch Conversion
- Only .mp4 files in the input directory will be converted
- Subdirectories are not scanned (only the top level)
- Output filenames will match input filenames (just with .mp3 extension)
- Original MP4 files are not deleted or modified

### Performance
- Large video files may take time to convert
- The progress bar shows overall progress
- For batch conversion, each file is converted sequentially
- You cannot start another conversion while one is in progress

## Error Handling

### Common Errors and Solutions

**"Input file does not exist"**
- Check that you've selected the correct file
- Ensure the file path is accessible

**"No MP4 files found in directory"**
- Make sure the input directory contains .mp4 files
- Check that you're using the correct directory

**"Error during conversion"**
- The video file may be corrupted
- Unsupported video format or codec
- Try converting a different file to isolate the issue

**"Output directory cannot be created"**
- Check that you have write permissions
- Ensure the disk is not full
- Try a different output location

## Troubleshooting

### Application won't start
- Make sure you're running Windows
- Check if your antivirus is blocking the file
- Right-click → Properties → Unblock (if needed)
- Run as Administrator if you get permission errors

### Conversion fails for specific files
- The file may be DRM-protected
- Unsupported codec or video format
- File may be corrupted
- Try playing the file in a media player to verify it's valid

### Progress bar doesn't move
- The file may be very large (just wait longer)
- The application might be frozen (check Task Manager)
- Try converting a smaller test file

### Output file is silent
- The source video may not have an audio track
- Check the original file in a media player
- Verify the volume settings in the player

## Technical Details

- **Built with**: Python 3.12, Tkinter, MoviePy
- **Supported input formats**: MP4, AVI, MKV, MOV, and other video formats
- **Output format**: MP3 (standard audio format)
- **Audio quality**: Same as source (no re-encoding of audio)

## Keyboard Shortcuts

- **Alt+S**: Switch to Single File mode
- **Alt+B**: Switch to Batch mode
- **Ctrl+O**: Browse for input (depends on active mode)
- **Enter**: Start conversion (if Convert button is focused)
- **Escape**: Exit application

## File Size Considerations

| Video Length | Expected MP3 Size | Approx. Conversion Time |
|--------------|-------------------|------------------------|
| 5 minutes    | ~5 MB             | 10-20 seconds          |
| 30 minutes   | ~30 MB            | 1-2 minutes            |
| 2 hours      | ~120 MB           | 5-8 minutes            |

*Times are estimates and vary based on CPU speed and file complexity*

## Support

If you encounter issues:
1. Check the log messages for specific error details
2. Try the troubleshooting steps above
3. Check that the source files play correctly in other players
4. Ensure you have sufficient disk space

## License

This is a standalone utility built for converting video to audio. Use it responsibly and respect copyright laws when converting copyrighted material.
