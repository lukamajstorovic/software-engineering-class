# LAB 6

## Start a new project

git clone https://gitlab.com/lukamajstorovic/se-labs-2223-prp.git
git config user.name "lukamajstorovic"
git config user.email "lmajstorovic@etfos.hr"
git remote add upstream https://gitlab.com/levara/se-labs-2223-prp
git fetch upstream master
git merge upstream/master
git status
mkdir lab6
cd lab6
cd ..
ls
cd lab6/
python -m venv env
source env/Scripts/activate
pip install django
django-admin startproject myimgur
ls
cd myimgur/
ls
python manage.py startapp app
ls
code .
python manage.py migrate
winpty python manage.py runserver
winpty python manage.py createsuperuser
winpty python manage.py runserver
git status
cd ..
git status
ls
git add myimgur/
git status
code ..
code ..
git status
git add ../.gitignore
git status
git commit -m "Add initial lab6 setup"
git status
git push origin master
git status
history
