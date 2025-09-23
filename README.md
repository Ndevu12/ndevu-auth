# Ndevu Auth - Secure Multi-Factor Authentication System

This is a complete authentication system built with SuperTokens, featuring Google and Apple OAuth providers with Multi-Factor Authentication (MFA) support.

## 🚀 Quick Start

### 1. Start SuperTokens Services
```bash
./start-services.sh
```

### 2. Start Backend
```bash
cd backend
source venv/bin/activate
python app.py
```

### 3. Start Frontend (in another terminal)
```bash
cd frontend
npm start
```

### 4. Access the Application
- **Ndevu Auth Frontend**: http://localhost:3000
- **Ndevu Auth API**: http://localhost:3008
- **SuperTokens Dashboard**: http://localhost:3567/dashboard

## 🛑 Stop All Services
```bash
./stop-services.sh
```

## 🔧 Features

- **OAuth Providers**: Google and Apple authentication
- **Multi-Factor Authentication**: OTP email verification (MFA enabled by default)
- **Account Linking**: Automatic linking of accounts across providers
- **Session Management**: Secure session handling with SuperTokens
- **CORS Support**: Proper cross-origin configuration
- **Modern UI**: Clean, responsive interface built with React

## 🐳 Docker Services

The application uses Docker Compose to run:
- **SuperTokens**: PostgreSQL-based instance on port 3567
- **PostgreSQL**: Database for SuperTokens on port 5432

### Manual Docker Commands
```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Check status
docker ps
```

## 🔧 Configuration

### Backend Configuration
- **File**: `backend/config.py`
- **SuperTokens URI**: `http://localhost:3567`
- **API Port**: 3008
- **Website Port**: 3000

### Frontend Configuration
- **File**: `frontend/src/config.tsx`
- **API Domain**: `http://localhost:3008`
- **Website Domain**: `http://localhost:3000`

## 🔐 OAuth Providers

### Google OAuth
- **Client ID**: `1060725074195-kmeum4crr01uirfl2op9kd5acmi9jutn.apps.googleusercontent.com`
- **Redirect URI**: `http://localhost:3000/auth/callback/google`

### Apple OAuth
- **Client ID**: `4398792-io.supertokens.example.service`
- **Redirect URI**: `http://localhost:3000/auth/callback/apple`

## 🧪 Testing OAuth

Test the OAuth endpoints:
```bash
# Google OAuth
curl "http://localhost:3008/auth/authorisationurl?thirdPartyId=google&redirectURIOnProviderDashboard=http%3A%2F%2Flocalhost%3A3000%2Fauth%2Fcallback%2Fgoogle"

# Apple OAuth
curl "http://localhost:3008/auth/authorisationurl?thirdPartyId=apple&redirectURIOnProviderDashboard=http%3A%2F%2Flocalhost%3A3000%2Fauth%2Fcallback%2Fapple"
```

## 📁 Project Structure

```
example-app/
├── backend/                 # FastAPI backend
│   ├── app.py              # Main application
│   ├── config.py           # SuperTokens configuration
│   └── requirements.txt    # Python dependencies
├── frontend/               # React frontend
│   ├── src/
│   │   ├── config.tsx      # SuperTokens React config
│   │   └── ...
│   └── package.json        # Node dependencies
├── docker-compose.yml      # Docker services
├── start-services.sh       # Start all services
├── stop-services.sh        # Stop all services
└── README.md              # This file
```

## 🔍 Troubleshooting

### Common Issues

1. **Port conflicts**: Make sure ports 3000, 3008, and 3567 are available
2. **Docker not running**: Ensure Docker is installed and running
3. **OAuth errors**: Check that redirect URIs match in provider consoles

### Logs
```bash
# Backend logs
cd backend && python app.py

# Docker logs
docker-compose logs -f

# Frontend logs
cd frontend && npm start
```

## 🎯 Next Steps

1. Configure OAuth providers in their respective developer consoles
2. Add the redirect URIs to your OAuth applications
3. Test the complete authentication flow
4. Customize the UI and add more features

## 📚 Resources

- [SuperTokens Documentation](https://supertokens.com/docs)
- [Google OAuth Setup](https://developers.google.com/identity/protocols/oauth2)
- [Apple Sign-In Setup](https://developer.apple.com/sign-in-with-apple/)
