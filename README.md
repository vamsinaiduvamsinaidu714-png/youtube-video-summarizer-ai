# YouTube Video Summarizer AI

An AI-powered web application that converts YouTube video transcripts into structured, easy-to-understand summaries using Google Gemini AI.

## Project Overview

YouTube Video Summarizer AI helps students, professionals, and technology enthusiasts save time by extracting important information from lengthy YouTube videos.

The application retrieves the available video transcript and uses Google's Gemini AI model to generate structured notes in the user's selected language.

It provides a simple interface where users can enter a YouTube URL, select a summary language, generate notes, and download the results.

## Key Features

- **Automatic Transcript Extraction:** Retrieves available transcripts from YouTube videos.
- **AI-Powered Summarization:** Generates structured summaries using Google Gemini.
- **Multilingual Output:** Supports English, Telugu, and Hindi summaries.
- **Video Thumbnail Preview:** Displays the YouTube video's thumbnail.
- **Structured Notes:** Organizes information into executive summaries, key takeaways, important concepts, actionable insights, and conclusions.
- **Downloadable Notes:** Allows users to download generated summaries as text files.
- **Simple Interface:** Built with Streamlit for an easy user experience.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Web application interface |
| Google Gemini API | AI-powered summarization |
| YouTube Transcript API | Transcript extraction |
| python-dotenv | Environment variable management |

## System Architecture

```text
       YouTube Video URL
               |
               v
      Extract Video ID
               |
               v
    YouTube Transcript API
               |
               v
       Extract Transcript
               |
               v
       Prompt Generation
    (Selected Output Language)
               |
               v
         Gemini AI API
               |
               v
     Structured AI Summary
               |
               v
       Streamlit Interface
               |
               v
        Download Notes
```

## Project Structure

```text
youtube-video-summarizer-ai/
|
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vamsinaiduvamsinaidu714-png/youtube-video-summarizer-ai.git
```

### 2. Navigate to the Project Directory

```bash
cd youtube-video-summarizer-ai
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Gemini API Key

Create a `.env` file in the project directory and add:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Obtain an API key through Google AI Studio.

Never upload your `.env` file or expose your API key publicly.

### 7. Run the Application

```bash
streamlit run app.py
```

Open the following URL in your browser:

```text
http://localhost:8501
```

## How to Use

1. Launch the application.
2. Paste a valid YouTube video URL.
3. Select the preferred summary language.
4. Click **Generate Summary**.
5. View the AI-generated notes.
6. Download the summary as a text file.

## Future Enhancements

- AI-generated revision bullet points.
- Interactive quizzes and flashcards.
- PDF export functionality.
- Improved multilingual transcript handling.
- AI-powered conversational learning assistant.
- Cloud deployment and public access.

## Project Status

**Current Version:** v1.1 – Multilingual Summarization Improvements

This project is actively under development, with additional AI-powered study and revision features planned.

## Author

**Vamsi Achanta**

GitHub: [vamsinaiduvamsinaidu714-png](https://github.com/vamsinaiduvamsinaidu714-png)

---

*Developed as a practical AI application engineering project using Python, Streamlit, and Google Gemini AI.*
