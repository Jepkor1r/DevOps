- A summary of setting up flask in virtual environment.
- Why virtual environment?
- - To address the issue of maintaining different versions of packages for different applications.
- First, create a directory where the project will live and navigate to it. 
- - For Example: 
             `mkdir demoproject`
             `cd demoproject`
- Now, create a virtual environment:
- - `python3 -m venv venv`
- In the above command, I'm asking Python to run the `venv` package, which creates a virtual environment named venv. If you find this confusing, you can replace the second venv with a different name that you want to assign to your virtual environment.
- To activate your brand new virtual environment:
- - `source venv/bin/activate`
- Your terminal should now be reading this:
- - `(venv) $ _`
- Now that you have a virtual environment created and activated, you can finally install Flask in it:
- - `pip install flask`
- If you want to confirm that your virtual environment now has Flask installed, you can start the Python interpreter and import Flask into it:
- - `python3` command then press ENTER
- - `import flask`
- If this statement does not give you any errors you can congratulate yourself, as Flask is installed and ready to be used.
- Let's create a package called app, that will host the application. Make sure you are in the demoproject directory and then run the following command:
- - `mkdir app`
- - `cd app`
- - `touch __init__.py` ~ <em>Flask application instance</em>
- - `touch routes.py` ~ <em>Home page route</em>
- Then change directory back to demoproject directory
- - `cd ..`
- - `touch miniblog.py` ~ <em>Main application module</em>

<strong> Just to make sure that you are doing everything correctly, below you can see a diagram of the project structure so far:</strong>
demoproject/
     venv/
     app/
         __init__.py
         routes.py
     miniblog.py

- Believe it or not, this first version of the application is now complete! Before running it, though, Flask needs to be told how to import it, by setting the FLASK_APP environment variable:
- - `export FLASK_APP=miniblog.py`
- You can run your first web application by typing:
- - `flask run`
- - Since this application is running in a development environment, Flask uses port 5000. Now open up your web browser and enter the following URL in the address field:
- - `http://localhost:5000/`
- - `http://localhost:5000/index`

- Alternatively:(This happens when the FLASK_APP variable isn't set or for just simplicity)
- From the project directory (project), execute:
- - `python3 miniblog.py`
- Test routes by opening your browser and navigate to:
- - `http://localhost:5000/`
- - `http://localhost:5000/index`
