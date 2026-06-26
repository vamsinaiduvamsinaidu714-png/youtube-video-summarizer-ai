import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import os

# -----------------------------

# Page Configuration

# -----------------------------

st.set_page_config(
page_title="YouTube Video Summarizer",
page_icon="🎥",
layout="centered"
)

# -----------------------------

# Load Environment Variables

# -----------------------------

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found in .env file")
    st.stop()

genai.configure(api_key=api_key)

# -----------------------------

# Prompt

# -----------------------------

PROMPT = """
You are an expert YouTube content analyst.

Analyze the transcript and provide:

1. Executive Summary
2. Key Takeaways (5 points)
3. Important Concepts
4. Actionable Insights
5. Final Conclusion

Keep the response clear and easy to understand.
"""

# -----------------------------

# Extract Transcript

# -----------------------------

def extract_transcript_details(youtube_url):
    try:


        if "watch?v=" in youtube_url:
            video_id = youtube_url.split("v=")[1].split("&")[0]

        elif "youtu.be/" in youtube_url:
            video_id = youtube_url.split("/")[-1]

        else:
            raise Exception("Invalid YouTube URL")

        api = YouTubeTranscriptApi()

        transcript_text = api.fetch(video_id)

        transcript = " ".join(
        [item.text for item in transcript_text]
        )

        return transcript

    except Exception as e:
        st.error(f"Transcript Error: {e}")
        return None

# -----------------------------

# Generate Summary

# -----------------------------

def generate_gemini_content(transcript_text):
    try:


        model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        response = model.generate_content(
            PROMPT + "\n\nTranscript:\n" + transcript_text
        )

        return response.text

    except Exception as e:
        st.error(f"Gemini Error: {e}")
        return None


# -----------------------------

# UI

# -----------------------------

st.title("🎥 YouTube Video Summarizer")

st.write(
"Generate AI-powered notes and summaries from any YouTube video."
)

youtube_link = st.text_input(
"Paste YouTube Video URL"
)

# Thumbnail Preview

if youtube_link:


    try:

        if "watch?v=" in youtube_link:
            video_id = youtube_link.split("v=")[1].split("&")[0]

        elif "youtu.be/" in youtube_link:
            video_id = youtube_link.split("/")[-1]

        else:
            video_id = None

        if video_id:
            st.image(
                f"https://img.youtube.com/vi/{video_id}/0.jpg",
                use_container_width=True
            )

    except:
        pass


# Generate Summary Button

if st.button("Generate Summary"):


    if not youtube_link:
        st.warning("Please enter a YouTube URL")

else:

    with st.spinner(
        "Fetching transcript and generating summary..."
    ):

        transcript_text = extract_transcript_details(
            youtube_link
        )

        if transcript_text:

            summary = generate_gemini_content(
                transcript_text
            )

            if summary:

                st.success(
                    "Summary Generated Successfully"
                )

                st.markdown(
                    "## 📝 Detailed Notes"
                )

                st.write(summary)

                st.download_button(
                    label="📥 Download Notes",
                    data=summary,
                    file_name="youtube_summary.txt",
                    mime="text/plain"
                )


# Footer

st.markdown("---")

st.caption(
"Built with Streamlit + Gemini AI"
)
