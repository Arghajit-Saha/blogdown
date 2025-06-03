# 📝 Blogdown — A Markdown-Powered Blogging Platform

Blogdown is a Django-based blogging platform that allows users to write blogs in **Markdown format**, see a **live HTML preview**, and publish them as readable blog posts. It also includes a **contact form** for user queries and a custom admin panel for managing users, blogs, and messages.

---

## 🚀 Features

- ✍️ **Markdown Blog Editor**: Write your blog in Markdown with real-time HTML preview.
- 🧠 **Auto Markdown-to-HTML Conversion**: Blogs are stored as Markdown and rendered into HTML on display.
- 💌 **Contact Form**: Visitors can send queries or feedback via a simple form.
- 👤 **Admin Panel**: Admins can view and manage users, blogs and contact forms.
- 📄 **Clean UI**: Built with usability in mind.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Live Preview**: JavaScript + [marked.js](https://github.com/markedjs/marked)

---

## 🧩 Folder Structure

```
blogdown/
├── adminpanel/         # Custom admin panel app
│   ├── views.py        # Admin authentication and dashboard views
│   ├── urls.py         # Admin panel URL routes
│   └── ...
├── blog/               # Core blog app
│   ├── models.py       # Blog, contact, user models
│   ├── views.py        # Blog creation, listing, contact form, user authentication
│   ├── urls.py         # Blog app URL routes
│   └── ...
├── static/             # Static files (CSS, fonts)
│   ├── css/
│   └── fonts/
├── templates/          # HTML templates
│   ├── admin-dashboard.html
│   ├── user.html
│   ├── blogs.html
│   ├── contact-admin.html
│   ├── ...
├── blogdown/           # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── manage.py
└── requirements.txt
```

---

## 🧪 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Arghajit-Saha/blogdown.git
   cd blogdown
   ```

2. **Create virtual environment and install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Apply migrations and run the server**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. **Open in Browser**

   Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the site.