import whisper
import os
import torch
import warnings

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Supported audio and video file extensions
SUPPORTED_EXTENSIONS = {".mp3", ".wav", ".m4a", ".mp4", ".mkv", ".avi", ".flv", ".mov"}

def find_audio_video_files(directory):
    """Search for audio and video files in the given directory."""
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    audio_video_files = [f for f in files if os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS]
    return audio_video_files

def transcribe_audio_video(file_path, device):
    """Transcribe an audio/video file using the Whisper model."""
    model = whisper.load_model("base", device=device)

    print(f"Transcribing {file_path} on {device.upper()}... This may take a while.")
    result = model.transcribe(file_path)

    transcript_file = os.path.splitext(file_path)[0] + "_transcript.txt"

    # Check if transcript file already exists
    if os.path.exists(transcript_file):
        choice = input(f"The file '{transcript_file}' already exists. Do you want to overwrite it? (yes/no): ").strip().lower()
        if choice not in ["yes", "y"]:
            print("Transcription aborted. The file was not overwritten.")
            return

    with open(transcript_file, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"Transcription complete. Saved to {transcript_file}")



if __name__ == "__main__":
    # Ask the user whether to use GPU or CPU
    if torch.cuda.is_available():
        device_choice = input("Would you like to use GPU or CPU? (enter 'gpu' or 'cpu'): ").strip().lower()
        device = "cuda" if device_choice == "gpu" else "cpu"
    else:
        print("GPU not available. Using CPU.")
        device = "cpu"

    choice = input("Do you want to enter a directory or scan the current folder? (enter 'dir' or 'local'): ").strip().lower()

    if choice == "dir":
        directory = input("Enter the directory to search for audio/video files: ").strip()
        if not os.path.isdir(directory):
            print("Error: Directory not found.")
            exit()
    elif choice == "local":
        directory = os.getcwd()
        print(f"Searching in the current folder: {directory}")
    else:
        print("Invalid choice. Please run the program again and enter 'dir' or 'local'.")
        exit()

    files = find_audio_video_files(directory)

    if not files:
        print("No audio or video files found.")
    else:
        print("Found the following audio/video files:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        try:
            choice = int(input("Select a file to transcribe (enter the number): ").strip())
            if 1 <= choice <= len(files):
                file_path = os.path.join(directory, files[choice - 1])
                transcribe_audio_video(file_path, device)
            else:
                print("Invalid choice. Please run the program again.")
        except ValueError:
            print("Invalid input. Please run the program again.")
