python virtual environment
==========================
.. code::bash
   python -m venv django_2_1_3
   cd django_2_1_3
   source bin/activate
   pip install django==2.1.3

   # Generate UML diagram of django app models
   # Need pacman -S graphivz first
   pip install pygraphviz
   pip install django-extensions==2.1.3
   # Add 'django_extensions' to INSTALLED_APPS in settings.py
   python manage.py graph_models -a -o myapp_models.png

docker
======
.. code::bash
   systemctl start docker.service
   docker build -t django .
   docker run -p 8000:8000 -i -t django /bin/bash
   # not yet succeed
