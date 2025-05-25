import streamlit as st
import groq
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()
# Set the model to LLaMA2-70b-4096 as it's available in the official documentation
model = "llama2-70b-4096"

# Initialize Groq client with API key
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))
#client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

def send_email(recipient_emails, summary):
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ", ".join(recipient_emails)  # Join multiple emails with commas
    message["Subject"] = "Your Meeting Summary"
    
    # Add body
    message.attach(MIMEText(summary, "plain"))
    
    try:
        # Create SMTP session
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Enable TLS
        server.login(sender_email, sender_password)
        
        # Send email
        server.send_message(message)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False

def generate_summary(transcript):
    prompt = """
    Please provide a comprehensive summary of the following transcript. 
    Focus on:
    1. Key points and main arguments
    2. Important decisions or conclusions
    3. Action items or next steps
    4. Any critical concerns or risks identified
    5. Number of people mentioned
    6. Name of the attendees and their roles
    Maintain objectivity and avoid bias in the summary.
    Format the summary in clear, concise paragraphs.
    
    Transcript:
    {transcript}
    """
    
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional summarizer that creates clear, unbiased summaries."
                },
                {
                    "role": "user",
                    "content": prompt.format(transcript=transcript)
                }
            ],
            model="llama-3.1-8b-instant",
            temperature=0.3,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def main():
    st.title("Transcript Summarizer")
    
    # Input fields
    st.write("Enter email addresses separated by commas (e.g., john@example.com, jane@example.com)")
    email_input = st.text_input("Enter recipient email addresses")
    transcript = st.text_area("Enter the transcript", height=300)
    
    if st.button("Generate Summary"):
        if not email_input or not transcript:
            st.error("Please fill in all fields")
            return
            
        # Process email addresses
        recipient_emails = [email.strip() for email in email_input.split(",")]
        
        with st.spinner("Generating summary..."):
            summary = generate_summary(transcript)
            
            st.subheader("Generated Summary")
            st.write(summary)
            
            # Send email with summary
            if send_email(recipient_emails, summary):
                st.success(f"Summary has been sent to {len(recipient_emails)} recipient(s)!")
            else:
                st.error("Failed to send email. Please try again.")
            
            # Option to download summary
            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="transcript_summary.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()