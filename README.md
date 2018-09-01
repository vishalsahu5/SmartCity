# SmartCity
Repository for the web application of the capstone project.

##Steps to setup development server
1. Clone this repository to your computer.
2. Create a virtual environment with python 3
3. Start the virtual environment.
4. Inside the top level project directory, run 

    ``pip install -r requirements.txt`` 
    
5. Run the following commands one by one

    ``python manage.py makemigrations``
    
    ``python manage.py makemigrations accounts``
    
    ``python manage.py makemigrations dustbin``
    
    ``python manage.py makemigrations parking``
    
    ``python manage.py migrate``
    
6. At last, run the command for start the server

    ``python manage.py runserver``