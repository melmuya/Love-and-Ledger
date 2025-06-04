# Love and Ledger

A modern web application built with Django and React.

## Project Structure

```
love-and-ledger/
├── client/             # React frontend
│   ├── src/           # Source files
│   ├── public/        # Static files
│   └── package.json   # Frontend dependencies
│
├── server/            # Django backend
│   ├── manage.py      # Django management script
│   └── requirements.txt # Backend dependencies
│
└── README.md          # This file
```

## Prerequisites

- Python 3.13+
- Node.js 18+
- npm or yarn
- Git

## Development Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd love-and-ledger
   ```

2. Backend Setup:
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   
   # Install dependencies
   cd server
   pip install -r requirements.txt
   
   # Run migrations
   python manage.py migrate
   
   # Start development server
   python manage.py runserver
   ```

3. Frontend Setup:
   ```bash
   # Install dependencies
   cd client
   npm install
   
   # Start development server
   npm run dev
   ```

## Development

- Backend runs on http://localhost:8000
- Frontend runs on http://localhost:5173

## Testing

- Backend tests: `python manage.py test`
- Frontend tests: `npm test`

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Submit a pull request

## License

[Your chosen license] 