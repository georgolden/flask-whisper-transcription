# Flask Audio Transcription App

A Flask web application that transcribes audio files using OpenAI's Whisper API.

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
- Docker (optional)

## Installation

### Option 1: Local Installation with Virtual Environment

1. Clone the repository:
```bash
git clone https://github.com/georgolden/flask-whisper-transcription.git
cd flask-whisper-transcription
```

2. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root:
```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

### Option 2: Docker Installation

1. Clone the repository:
```bash
git clone https://github.com/georgolden/flask-whisper-transcription.git
cd flask-whisper-transcription
```

2. Create a .env file with your OpenAI API key:
```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

3. Build and run the Docker container:
```bash
# Build the image
docker build -t flask-whisper-app .

# Run the container
docker run -d -p 5000:5000 --env-file .env flask-whisper-app
```

## Usage

### Running Locally

1. Activate the virtual environment (if not already activated):
```bash
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

2. Start the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

### Running with Docker

1. The application will be available at:
```
http://localhost:5000
```

2. To stop the container:
```bash
docker ps  # Find the container ID
docker stop <container-id>
```

## Development

### Virtual Environment Tips
- Always activate the virtual environment before working on the project
- If you install new packages, update requirements.txt:
```bash
pip freeze > requirements.txt
```
- To deactivate the virtual environment:
```bash
deactivate
```

### Docker Development Tips
- Rebuild the image after making changes:
```bash
docker build -t flask-whisper-app .
```
- View logs:
```bash
docker logs <container-id>
```
- Access container shell:
```bash
docker exec -it <container-id> bash
```

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
