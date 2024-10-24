# Sports Database Project (CS2300)
Source code for a web-based sports database. Created by Benjamin Biehl and Brant Bremer.

## Setup for Windows
Install latest version of python using the following link:
* https://www.python.org/downloads/windows/

Run the following command in console to download Django:
```console
py -m pip install Django
```

## Setup for Mac
Install latest version of python using the following link:
* https://www.python.org/downloads/macos/

Run the following command in console to download Django:
```console
python -m pip install Django
```

## How to code various things
To run the server, simply run the following command and go to the url provided:
```console
python manage.py runserver
```
If you'd like to access the admin site, add */admin* at end end of the URL.

To register a new admin user, use the following command:
```console
python manage.py createsuperuser
```
And follow the steps to create a new admin user.

If you want to add tables to the database itself, navigate to *main/models.py*, and add a class.
Make sure to migrate the changes to the database by running the following commands:
```console
python manage.py migrate
python manage.py makemigrations main
```

To update the changes in the admin page, naviage to *main/admin.py*, and import the class.

To add a new view, nativate to *main/views.py*, and add the view there.

To add a new url, naviage to *main/urls.py*, and update the url path there.

## TODO
- [x] Setup Django
- [x] Initialize Database
- [ ] Setup Login
- [ ] Add all necessary classes
- [ ] Main page
- [ ] User page
- [ ] Sports page
- [ ] Functions
- [ ] UI