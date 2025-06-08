
---

# Scheduled_Notification_System

## Backend Setup

1. Create and activate Python virtual environment with **uv**:

```bash
uv venv
```

2. Activate the Virtual Envirnment
```bash
# Linux / Mac
source .venv/bin/activate 

# Windows (PowerShell)
.venv\Scripts\activate (on Windows)

```

3. Install dependencies from your TOML file:

```bash
uv pip install -r pyproject.toml
```

4. Run migrations:

```bash
# Linux / Mac
python3 manage.py migrate (on Linux/Mac)

# Windows (PowerShell)
python3 .\manage.py migrate 

```

5. Start backend:

```bash
# Linux / Mac
python3 manage.py runserver

# Windows (PowerShell)
python .\manage.py runserver 
```

Backend runs on `http://localhost:8000`

---

## Frontend Setup (Angular)

1. Go to frontend folder:

```bash
cd frontend
```

2. Install npm packages:

```bash
npm install
```

3. Run Angular app:

```bash
ng serve
```

Frontend runs on `http://localhost:4200`

---

## Run both servers and open frontend URL to use the app.

---

