# QuartzOS: Unified AI Agent System for Quartz Visualz

QuartzOS is a modular AI-powered operating system for creative agencies, designed to automate and streamline client management, content creation, project updates, and more. Each agent is a separate Python module, working together as services.

## Agents Overview

- **LeadBot**: Reads leads from Gmail, Zapier forms, and Instagram DMs (mock via webhook). Uses GPT-4 to detect service type and urgency. Auto-schedules via Calendly.
- **ReplyGenie**: Drafts personalized responses for client queries, adapting to tone and context.
- **SocialAgent**: Generates content ideas, captions, hashtags, and posts via Buffer API. Supports weekly content planning.
- **EditorBot**: Organizes video files, labels audio via Whisper, and suggests basic edits.
- **ClientMailer**: Sends weekly project status updates to clients via customized emails.
- **FeedbackAI**: Collects and summarizes feedback from Google Forms.
- **InvoiceBot**: Generates and sends PDF invoices based on project data in spreadsheets.

## Features
- Modular folder structure: Each agent in its own file.
- .env support for API keys and credentials.
- Central dashboard (`main.py` or Streamlit) to trigger tasks manually or via schedule.
- CSV and Google Sheets integration.
- Streamlit dashboard for manual triggers and log viewing.

## Setup

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a `.env` file** with your API keys and credentials (see `.env.example`).
4. **Run the dashboard**:
   ```bash
   streamlit run main.py
   ```

## Usage
- Use the Streamlit dashboard to trigger agents, view logs, and monitor status.
- Agents can also be scheduled or triggered via API/webhooks.

## Folder Structure
```
QuartzOS/
├── agents/
│   ├── leadbot.py
│   ├── replygenie.py
│   ├── socialagent.py
│   ├── editorbot.py
│   ├── clientmailer.py
│   ├── feedbackai.py
│   └── invoicebot.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first.

## License
[MIT](LICENSE) 