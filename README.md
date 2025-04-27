
# Django Fun Project

Hey there!  
This is just a fun little Django project I'm working on to sharpen my web development skills. Nothing too serious — just experimenting, learning, and enjoying the process.
Feel free to check it out, suggest improvements, or point out any mistakes. I'd really appreciate it!

## How to Run

1. **Clone the project**  
   ```bash
   git clone <your-repo-url>
   cd <project-folder>
   ```

2. **Create a virtual environment** (recommended)  
   ```bash
   python3 -m venv venv  # On Windows: python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   - Copy the `.env.template` file and create your own `.env` file.
   - Fill in the necessary settings.

5. **Run migrations**  
   ```bash
   python3 manage.py migrate
   ```

6. **Start the server**  
   ```bash
   python3 manage.py runserver
   ```

7. **Open your browser** and go to `http://127.0.0.1:8000/`

---

**Notes:**  
- This project uses `django-environ` to handle environment variables.
- It's mostly a playground for me to practice, so don’t expect a polished app (yet!).
- **Suggestions, edits, or feedback are always welcome!**

