# AI Text Summarization

## Project Description
AI Text Summarization is a web application that converts long paragraphs into short and meaningful summaries using Artificial Intelligence.

## Demo Link
https://text-summarization-ewyp2dhci7hycgeh7vjffh.streamlit.app/

## Features
- Summarizes long text
- Short, Medium, and Long summary options
- Displays original word count
- Displays summary word count
- Simple and user-friendly interface

## Technologies Used
- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- BART Model

## Project Structure
```text
Text Summarization/
├── app.py
├── requirements.txt
└── README.md
```

## Installation
Install the required libraries using:

```bash
py -m pip install -r requirements.txt
```

## Run the Application
Run the following command:

```bash
py -m streamlit run app.py
```

## How to Use
1. Open the application in your browser.
2. Enter or paste a paragraph.
3. Select the summary length.
4. Click the **Summarize Text** button.
5. View the generated summary.

## AI Model
This project uses the pretrained `facebook/bart-large-cnn` model from Hugging Face to generate summaries.

## Future Enhancements
- Support PDF and text file uploads
- Add multiple language support
- Allow users to download summaries
