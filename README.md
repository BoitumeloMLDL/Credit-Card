# Loan Default Probability Calculator

This project is a web application to calculate the probability of loan default based on user input. The stack consists of:

- **Frontend:** Vue (via CDN) with Bootstrap for styling, served via a simple web server.
- **Backend:** FastAPI with SQLite for data storage.
- **Deployment:** Dockerized application deployed to DigitalOcean using SSH-based deployment scripts.

## Project Structure

```

.
├── backend/ # FastAPI application
│ ├── main.py # Main FastAPI app
│ ├── models.py # Database models
│ ├── requirements.txt # Backend dependencies
│ └── ... # Other backend files
├── frontend/ # Vue-based frontend
│ ├── index.html # Main application HTML
│ ├── assets/ # Static files
│ └── ... # Other frontend files
├── docker-compose.yml # Docker configuration
├── README.md # Project documentation
└── .env # Environment variables
```

## Prerequisites

Ensure you have the following installed:

- **Python 3.11+** (for FastAPI backend)
- **Node.js (npx)** (for frontend development)
- **Docker & Docker Compose** (for deployment)

## Development Setup

To run the application locally, use the following command:

```bash
fastapi dev backend/main.py & npx server frontend/
```

### Explanation:

- `fastapi dev backend/main.py` runs the FastAPI backend with hot-reloading.
- `npx server frontend/` serves the frontend via a simple HTTP server.

Once running, access the application:

- **Frontend:** `http://localhost:3000`
- **Backend API:** `http://localhost:8000`

## API Endpoint

### `POST /default`

**Request Body:**

```json
{
  "amount_requested": 50000,
  "application_date": "2025-01-26",
  "risk_score": 700,
  "debt_to_income_ratio": 35.5
}
```

**Response:**

```json
0.92
```

## Deployment to DigitalOcean

The application is containerized using Docker and deployed to DigitalOcean using SSH-based deployment scripts.

### Deployment Steps:

1. Ensure DigitalOcean Droplet is set up with Docker.
2. Copy project files to the server using SSH:

   ```bash
   scp -r . tumi@your-server-ip:/path/to/app
   ```

3. SSH into the server:

   ```bash
   ssh tumi@your-server-ip
   ```

4. Run the application:

   ```bash
   docker compose up -d
   ```

5. Access the deployed app via `http://your-server-ip`.

## Docker Usage

To run the application locally using Docker:

1. Build and start the containers:

   ```bash
   docker compose up -d
   ```

2. Stop the containers:

   ```bash
   docker compose down
   ```

## Environment Variables

Create a `.env` file in the root directory with the following content:

```ini
FE_DEV_PORT=3000
DATABASE_URL=sqlite:///data/database.db
```

## Features

- Responsive frontend with Bootstrap
- Server-side and client-side validation
- Simple deployment process using Docker and SSH
- SQLite as the lightweight database
