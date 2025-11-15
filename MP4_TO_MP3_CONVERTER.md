# MP4 to MP3 Converter

A simple command-line tool to convert MP4 video files to MP3 audio files using moviepy.

## Installation

First, make sure you have the required dependencies:

```bash
pip install moviepy
```

Or install from the requirements file:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Conversion

Convert a single MP4 file to MP3:

```bash
python src/skill_seekers/cli/mp4_to_mp3_converter.py video.mp4 audio.mp3
```

Or with auto-generated output name (same name, .mp3 extension):

```bash
python src/skill_seekers/cli/mp4_to_mp3_converter.py video.mp4
```

### Batch Conversion

Convert all MP4 files in a directory:

```bash
python src/skill_seekers/cli/mp4_to_mp3_converter.py --batch ./videos ./mp3s
```

This will:
- Find all `.mp4` files in the `./videos` directory
- Convert each to MP3
- Save the MP3 files in the `./mp3s` directory

### Multiple Specific Files

Convert specific MP4 files to specific MP3 files:

```bash
python src/skill_seekers/cli/mp4_to_mp3_converter.py --files video1.mp4:audio1.mp3 video2.mp4:audio2.mp3
```

## Command Line Options

```
positional arguments:
  input_file            Input MP4 file path
  output_file           Output MP3 file path (optional)

optional arguments:
  -h, --help            Show help message and exit
  --version             Show version information
  -v, --verbose         Enable verbose output
  -q, --quiet           Suppress output messages

modes:
  --batch INPUT_DIR OUTPUT_DIR
                        Batch convert all MP4 files in a directory
  --files FILE_PAIRS [FILE_PAIRS ...]
                        Convert specific files (format: input.mp4:output.mp3)
```

## Examples

### Example 1: Single File Conversion

```bash
# Convert music_video.mp4 to music_video.mp3
python src/skill_seekers/cli/mp4_to_mp3_converter.py music_video.mp4

# Convert to a specific output name
python src/skill_seekers/cli/mp4_to_mp3_converter.py music_video.mp4 my_audio.mp3

# Verbose mode
python src/skill_seekers/cli/mp4_to_mp3_converter.py -v music_video.mp4
```

### Example 2: Batch Conversion

```bash
# Convert all MP4 files from ./videos to ./audio
python src/skill_seekers/cli/mp4_to_mp3_converter.py --batch ./videos ./audio

# Quiet mode (no output)
python src/skill_seekers/cli/mp4_to_mp3_converter.py -q --batch ./videos ./audio
```

### Example 3: Multiple Specific Files

```bash
# Convert specific files
python src/skill_seekers/cli/mp4_to_mp3_converter.py --files \
  concert1.mp4:concert_audio1.mp3 \
  concert2.mp4:concert_audio2.mp3 \
  lecture.mp4:lecture_audio.mp3
```

## Integration with Claude Code

This tool can be integrated into Claude Code as a skill by:

1. **Direct Execution**: Use the tool directly from Claude Code:
   ```bash
   python src/skill_seekers/cli/mp4_to_mp3_converter.py input.mp4 output.mp3
   ```

2. **As a Claude Tool**: Add to the MCP server configuration to expose this functionality to Claude.

## Error Handling

The converter handles various error scenarios:

- **File not found**: Displays an error message if the input file doesn't exist
- **Invalid paths**: Checks if input is a valid file/directory
- **Conversion errors**: Catches and reports any moviepy errors
- **Keyboard interrupt**: Gracefully handles Ctrl+C

## Requirements

- Python 3.6+
- moviepy 1.0.3+
- ffmpeg (automatically installed with moviepy)

## License

This tool is part of the Skill Seekers project.
