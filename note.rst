python virtual environment
==========================
.. code::bash
   python -m venv django_2_1_3
   cd django_2_1_3
   source bin/activate
   pip install django==2.1.3

docker
======
.. code::bash
   systemctl start docker.service
   docker build -t django .
   docker run -p 8000:8000 -i -t django /bin/bash
   # not yet succeed
