# Audio/Video Transcription Tool

This Python tool allows you to transcribe audio and video files into text using OpenAI's Whisper model. It provides the option to either scan a directory for files or manually select a file for transcription. You can also choose to run the transcription on either a CPU or GPU.

## Requirements

- Python 3.8 or higher
- Virtual Environment (recommended)
- `whisper` library
- `torch` library
- `ffmpeg` (for video/audio processing)

### Installing Dependencies

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Transcript-Creator.git

2. cd Transcript-Creator

3. python -m venv .venv recommended

4. Activate The Virtual Enviroment
 Windows: .venv\Scripts\activate 
  MacOS/Linux: source .venv/bin/activate 

5. pip install -r requirements.txt

6. You will need to install ffmpeg. Would recommend searching up a Youtube video on how to install
    [https://ffmpeg.org/download.html](url)
   
7. The program will prompt with overriding a prior transcript that's already been created say "yes" if you want to override it, or if it was never made

8. You can specify a directory or just say local and search the given folder

