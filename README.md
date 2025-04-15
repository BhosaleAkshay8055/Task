# 🚀 API

This project is a FastAPI-based backend application with PostgreSQL as the database. Follow the steps below to set it up on your local machine.

---

## 📦 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/BhosaleAkshay8055/Task.git
cd Task
```

### 2. Create and Activate a Virtual Environment

#### On Windows
```bash
python -m venv myenv
cd myenv\Scripts
./activate
```

> ⚠️ If you encounter a permissions issue, run this in PowerShell:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
Then activate the environment again:
```bash
myenv\Scripts\Activate.ps1
```

#### On macOS/Linux
```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🗃️ Database Setup

Make sure PostgreSQL is running on your system. Create a database and use the following format to set your `DATABASE_URL`:

```
postgresql://<username>:<password>@localhost:5432/<your-database-name>
```

Example:
```
postgresql://postgres:odoo@localhost:5432/vibeosysDb
```

You can place this in an `.env` file if using environment variables.

---

## ▶️ Run the Application
```bash
uvicorn main:app --reload
```

The server will start at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## ✅ API Docs

Once the server is running, you can explore the API at:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛠️ Tech Stack

- Python
- FastAPI
- PostgreSQL
- Uvicorn
- SQLAlchemy / Pydantic (if applicable)

---

## 📄 License

This project is licensed under the MIT License.
