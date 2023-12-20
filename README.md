# Virtual Guide: Exhibition Virtual Assistants

## Overview
This project is a detailed study on human-computer interaction and focused on developing a virtual assistant in exhibition settings. The assistant combines several advanced AI models and technologies. Key components include:

- **PyQt6 & Python:** The user interface, crafted using PyQt6 and Python 3.8, features a layout with a virtual face and a chat area, facilitating interactive communication.
- **Speech-to-Text:** Leveraging OpenAI's Whisper model for efficient speech-to-text conversion, the system can accurately transcribe user queries.
- **Text Understanding & Response:** Utilizing Hugging Face's QA models, the virtual assistant comprehensively understands and responds to text inputs.
- **Text-to-Speech:** A combination of Tacotron2 and WaveNet generates natural-sounding speech responses, ensuring a seamless conversational flow.
- **Image Analysis & Interaction:** The assistant employs image analysis to detect the user's face, allowing the model's eyes to follow the user's movements, creating a more engaging and interactive experience.

## Usage
To get started with the Virtual Guide desktop application, follow these steps:

1. **Install Dependencies:** First, ensure that all required dependencies are installed. Open your command line interface and execute the following command:
   ```
   pip install -r requirements.txt
   ```
   This will install all the necessary libraries and tools as listed in the `requirements.txt` file.

2. **Run the Application:** Once the dependencies are successfully installed, you can launch the application by running `main.py`. To do this, use the following command in your command line interface:
   ```
   python main.py
   ```
   This will initiate the desktop app, displaying the virtual assistant interface with the interactive face and chat functionalities.
