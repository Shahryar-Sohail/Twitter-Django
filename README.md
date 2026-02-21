  # 🐦 Django Twitter Clone 🚀

A modern, fully functional social media platform built with Django and Tailwind CSS. This project demonstrates clean CRUD operations, secure authentication, and a polished UI. 💻✨

---

## 🌟 Key Features
- **🔐 Secure Authentication:** Full Sign-up, Log-in, and Log-out workflows.
- **📝 Tweet Management:** Create, Read, Update, and Delete (CRUD) posts.
- **🎨 Modern UI:** Styled with **Tailwind CSS** and **daisyUI** 5.0.
- **🖤 Custom Styling:** Inputs feature bold black outlines and minimalist design.
- **📂 Media Support:** Image upload functionality for tweets.
- **📱 Responsive:** Fully optimized for both Desktop and Mobile views.

---

## 🛠️ Tech Stack
- **Backend:** [Django](https://www.djangoproject.com/) (Python) 🐍
- **Frontend:** [Tailwind CSS](https://tailwindcss.com/) & [daisyUI](https://daisyui.com/) 🎨
- **Database:** [SQLite](https://www.sqlite.org/) 🗄️
- **Styling Bridge:** `django-tailwind` 🌉

---

## 🚀 Installation & Local Setup

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/Shahryar-Sohail/Twitter-Django.git](https://github.com/Shahryar-Sohail/Twitter-Django.git)
cd Twitter-Django
python -m venv .venv
```

# Activate on Windows:
```bash
.venv\Scripts\activate
```
# Activate on Mac/Linux:
```bash
source .venv/bin/activate
```
```bash
pip install -r twitter/requirements.txt
```
```bash
cd twitter
python manage.py migrate
```
```bash
python manage.py tailwind install
python manage.py tailwind build
```
# Launch the Server 🚀
```bash
python manage.py runserver
```
## Visit http://127.0.0.1:8000/ and start tweeting! 🥳

# 📂 Project Structure
## twitter/ - Project configuration and root.

## tweet/ - Main application logic (Models, Views, Templates).

## theme/ - Tailwind CSS configuration and source files.

## media/ - Uploaded tweet images.


