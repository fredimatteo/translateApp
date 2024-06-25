# DeepL Translation App

This is a simple translation application built with Python and Streamlit. It uses the DeepL API for translation services. The application allows users to input text and select the target language for translation. It also provides an option to adjust the formality of the translation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
    ```
    git clone https://github.com/fredimatteo/translateApp.git
    ```
2. Navigate to the project directory:
    ```
    cd translateApp
    ```
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
4. Create a `.env` file in the root directory and add your DeepL API key:
    ```
    DEEPL_AUTH_KEY="your-deepl-api-key"
    ```
5. Run the Streamlit app:
    ```
    streamlit run src/app.py
    ```
The application should now be running at `http://localhost:8501`.

## Usage

Once the application is running, you can input text into the chat input field, select the target language and adjust the formality of the translation. The translated text will be displayed on the screen.