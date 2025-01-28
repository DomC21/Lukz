# Lukz Financial Analysis Platform

A comprehensive financial analysis platform leveraging the Unusual Whales API to provide actionable market insights.

## Features

- Real-time analysis of Congress trades, insider activity, and premium flow data
- AI-powered insights using ChatGPT for instant market interpretation
- Dynamic visualizations showcasing market trends and opportunities
- Modern, responsive UI with Tailwind CSS and shadcn/ui components

## Project Structure

```
.
├── backend/           # FastAPI backend service
│   ├── app/          # Application code
│   │   ├── main.py   # FastAPI application entry point
│   │   └── services/ # Business logic and API integrations
│   └── tests/        # Backend tests
└── frontend/         # React frontend application
    ├── src/          # Source code
    │   ├── components/ # React components
    │   └── hooks/    # Custom React hooks
    └── public/       # Static assets
```

## Development

### Prerequisites

- Python 3.12+
- Node.js 18+
- Unusual Whales API key

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Create a `.env` file with your Unusual Whales API key:
```
UNUSUAL_WHALES_API_KEY=your_api_key_here
```

4. Start the development server:
```bash
poetry run uvicorn app.main:app --reload
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file:
```
VITE_API_URL=http://localhost:8000
```

4. Start the development server:
```bash
npm run dev
```

## License

[MIT License](LICENSE)
