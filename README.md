# Flask Audio Transcription App

A simple Flask web application that transcribes audio files using OpenAI's Whisper API.

## Features

- Drag-and-drop interface for audio file upload
- Supports multiple audio formats (mp3, mp4, wav, m4a)
- Real-time transcription using OpenAI's Whisper API
- Automatic file cleanup
- Detailed error logging
- Progress status updates
- Automatic transcription file download

## Prerequisites

- Python 3.8+
- OpenAI API key
- Flask
- python-dotenv

## Installation

1. Clone the repository:
```bash
git clone https://github.com/georgolden/flask-whisper-transcription.git
cd flask-whisper-transcription
```

2. Install required packages:
```bash
pip install flask openai python-dotenv
```

3. Create a .env file in the project root:
```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

## Usage

1. Start the application:
```bash
python3 app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Upload an audio file by dragging and dropping or using the file selector

4. Wait for transcription to complete

5. Transcription will automatically download as a text file

## Supported File Formats

- MP3 (.mp3)
- MP4 (.mp4)
- WAV (.wav)
- M4A (.m4a)

## File Size Limits

- Maximum file size: 25MB
- File size limits are enforced by both the application and OpenAI's API

## Error Handling

The application includes comprehensive error handling for:
- Invalid API keys
- File format validation
- Size limit validation
- API errors
- File system errors

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
