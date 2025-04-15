# 🚀 Vibeosys API

This project is a FastAPI-based backend application with PostgreSQL as the database. Follow the steps below to set it up on your local machine.

---

## 📦 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create and Activate a Virtual Environment
On Windows
bash
Copy
Edit
python -m venv myenv
myenv\Scripts\Activate.ps1
⚠️ If you encounter a permissions issue, run this in PowerShell:

powershell
Copy
Edit
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Then activate the environment again:

bash
Copy
Edit
myenv\Scripts\Activate.ps1
On macOS/Linux
bash
Copy
Edit
python3 -m venv myenv
source myenv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🗃️ Database Setup
Make sure PostgreSQL is running on your system. Create a database and use the following format to set your DATABASE_URL:

php-template
Copy
Edit
postgresql://<username>:<password>@localhost:5432/<your-database-name>
Example:

bash
Copy
Edit
postgresql://postgres:odoo@localhost:5432/vibeosysDb
You can place this in an .env file if using environment variables.

▶️ Run the Application
bash
Copy
Edit
uvicorn main:app --reload
The server will start at http://127.0.0.1:8000

✅ API Docs
Once the server is running, you can explore the API at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc
