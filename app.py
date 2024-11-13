from flask import Flask, render_template, request, send_file
import openai
import os
import logging
from werkzeug.utils import secure_filename
import tempfile
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 26 * 1024 * 1024  # 26MB max file size
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    if not os.getenv('OPENAI_API_KEY'):
        logger.error("No API key found")
        return "Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.", 500
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    filepath = None
    output_filepath = None

    try:
        if not os.getenv('OPENAI_API_KEY'):
            raise ValueError("OpenAI API key not set in environment variables")
        
        if 'file' not in request.files:
            logger.error("No file part in request")
            return 'No file uploaded', 400
        
        file = request.files['file']
        if file.filename == '':
            logger.error("No selected file")
            return 'No file selected', 400

        if not file.filename.lower().endswith(('.mp3', '.mp4', '.wav', '.m4a')):
            logger.error(f"Invalid file format: {file.filename}")
            return 'Invalid file format. Please upload an mp3, mp4, wav, or m4a file.', 400

        # Save the uploaded file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        output_filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"transcription_{Path(filename).stem}.txt")
        
        logger.info(f"Processing file: {filename}")
        file.save(filepath)

        # Check if file was saved successfully
        if not os.path.exists(filepath):
            raise Exception("Failed to save uploaded file")

        # Check file size
        file_size = os.path.getsize(filepath)
        if file_size == 0:
            raise ValueError("Uploaded file is empty")
        logger.info(f"File size: {file_size} bytes")

        # Transcribe the audio file using new API syntax
        logger.info("Starting transcription")
        with open(filepath, 'rb') as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )

        if not transcript:
            raise ValueError("No transcription generated")

        # Save transcription
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(transcript)

        logger.info("Transcription completed successfully")

        # Send the transcription file
        return send_file(
            output_filepath,
            as_attachment=True,
            download_name=f"transcription_{Path(filename).stem}.txt",
            mimetype='text/plain'
        )

    except openai.AuthenticationError as e:
        logger.error(f"Authentication Error: {str(e)}")
        return "Invalid OpenAI API key. Please check your environment variables.", 401

    except openai.APIError as e:
        logger.error(f"OpenAI API Error: {str(e)}")
        return "OpenAI API service error. Please try again later.", 503

    except ValueError as ve:
        logger.error(f"Value Error: {str(ve)}")
        return str(ve), 400

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return f"An unexpected error occurred: {str(e)}", 500

    finally:
        # Clean up files
        try:
            if filepath and os.path.exists(filepath):
                os.remove(filepath)
            if output_filepath and os.path.exists(output_filepath):
                os.remove(output_filepath)
        except Exception as e:
            logger.error(f"Error cleaning up files: {str(e)}")

if __name__ == '__main__':
    # Check for API key at startup
    if not os.getenv('OPENAI_API_KEY'):
        logger.error("OpenAI API key not found in environment variables")
        print("Error: Please set the OPENAI_API_KEY environment variable")
    else:
        logger.info("Starting Flask application")
        app.run(debug=True)
