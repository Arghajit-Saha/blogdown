# 📝 Blogdown — A Markdown-Powered Blogging Platform

Blogdown is a Django-based blogging platform that allows users to write blogs in **Markdown format**, see a **live HTML preview**, and publish them as readable blog posts. It also includes a **contact form** for user queries.

---

## 🚀 Features

- ✍️ **Markdown Blog Editor**: Write your blog in Markdown with real-time HTML preview.
- 🧠 **Auto Markdown-to-HTML Conversion**: Blogs are stored as Markdown and rendered into HTML on display.
- 💌 **Contact Form**: Visitors can send queries or feedback via a simple form.
- 📄 **Clean, Responsive UI**: Built with usability in mind.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Live Preview**: JavaScript + Markdown parsing (e.g. `marked.js`)

---

## 🧩 Folder Structure
```
blogdown/
├── blog/ # Core blog app
│ ├── models.py # Blog and contact models
│ ├── views.py # Blog creation, listing, contact form handling
│ └── urls.py # Handles url routes
├── static/ # Static files (CSS, fonts)
├── blogdown/ # Project settings
├── templates/ # HTML templates
└── manage.py
```

---

## 🧪 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Arghajit-Saha/blogdown.git
   cd blogdown

2. **Create virtual environment and install dependencies**

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
3. **Apply migrations and run the server**

    ```bash
    python manage.py migrate
    python manage.py runserver

4. **Open in Browser**

    Navigate to http://127.0.0.1:8000/ to view the site.

    

