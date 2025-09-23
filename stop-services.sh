#!/bin/bash

echo "🛑 Stopping all services..."

# Stop the application servers
pkill -f "python app.py" 2>/dev/null
pkill -f "vite" 2>/dev/null
pkill -f "node.*vite" 2>/dev/null

# Stop Docker services
docker-compose down

echo "✅ All services stopped successfully!"
