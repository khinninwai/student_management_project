# 🎓 Student Management System (Django Project)

A Web Application built with Python and Django framework to manage student records efficiently. This application allows users to perform CRUD (Create, Read, Update, Delete) operations on student details.

---

## 📌 Project Overview & Workflow

The application follows Django's standard **MVT (Model-View-Template)** architectural pattern:

1. **Model Layer (`students/models.py`)**:
   - Defines the `Student` schema containing attributes: `first_name`, `last_name`, `email`, `date_of_birth`, and `enrollment_date`.
2. **View & Form Layer (`students/views.py`, `students/forms.py`)**:
   - Uses Django `ModelForm` for seamless form validation and handling data input.
   - Provides views for:
     - Home Dashboard (`home`)
     - Listing all students (`student_list`)
     - Adding a new student (`student_create`)
     - Updating existing student details (`student_update`)
3. **Template Layer (`students/templates/`)**:
   - `home.html` - Welcome page and main navigation.
   - `student_list.html` - Table displaying registered students with edit actions.
   - `student_form.html` - Dynamic form used for both adding and editing student details.
4. **URL Routing (`urls.py`)**:
   - Maps views to web endpoints for smooth browser navigation.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** Django
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/khinninwai/student_management_project.git](https://github.com/khinninwai/student_management_project.git)
cd student_management_project
