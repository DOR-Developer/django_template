How to Start a Django project:

1. Create and activate a virtual environment:
   - python -m venv env
   - ./env/Scripts/activate or /env/bin/activate
2. (Optional) Initialize git repository:
   - git init
   - create .gitignore
   - do not version control "env" folder and ".gitignore"
3. Install django:
   - pip install django
4. Create project:
   - django-admin startproject [project_name]
5. Create app:
   - go to project folder
   - python manage.py startapp [app_name]
6. Create folder structure:
   - Create on project folder templates and static folders
   - Create on static folder js, css, img and misc folders
   - do not version control "misc" and "img"
   - Create on app folder forms.py file