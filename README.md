# Meeting Transcript Summarizer

A Streamlit-based web application that generates comprehensive summaries of meeting transcripts using the Groq AI model and sends them via email.

## Features

- Web-based interface for transcript input
- AI-powered summary generation
- Email delivery of summaries
- Downloadable summary files
- Secure handling of sensitive information

## Prerequisites

- Python 3.8 or higher
- Groq API key
- Gmail account for sending emails

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variables:
```
GROQ_API_KEY=your_groq_api_key
EMAIL_USER=your_gmail_address
EMAIL_PASSWORD=your_gmail_app_password
```

## Configuration

### Email Setup
1. Use a Gmail account
2. Enable 2-factor authentication
3. Generate an App Password for the application
4. Use the App Password in the `.env` file

### Groq API Setup
1. Sign up for a Groq account
2. Generate an API key
3. Add the API key to the `.env` file

## Usage

1. Start the application:
```bash
streamlit run Main.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Enter your email address and paste the meeting transcript

4. Click "Generate Summary" to process the transcript

5. The summary will be:
   - Displayed on the web interface
   - Sent to your email
   - Available for download

## Summary Content

The generated summary includes:
- Key points and main arguments
- Important decisions or conclusions
- Action items or next steps
- Critical concerns or risks
- Number of people mentioned
- Names and roles of attendees

## Security Considerations

- API keys and credentials are stored in environment variables
- Email transmission uses TLS encryption
- No sensitive data is stored on the server

## Error Handling

The application handles various error scenarios:
- Missing input fields
- API connection issues
- Email sending failures
- Invalid email addresses

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Specify your license here]

## Support

For support, please [specify contact information or support channels]