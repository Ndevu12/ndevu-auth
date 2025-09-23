#!/bin/bash

echo "🚀 Starting SuperTokens and PostgreSQL..."
docker-compose up -d

echo "⏳ Waiting for services to be ready..."
sleep 10

echo "✅ Services started successfully!"
echo "📊 SuperTokens Dashboard: http://localhost:3567/dashboard"
echo "🔧 SuperTokens API: http://localhost:3567"

echo ""
echo "To start your application:"
echo "1. Backend: cd backend && source venv/bin/activate && python app.py"
echo "2. Frontend: cd frontend && npm start"
