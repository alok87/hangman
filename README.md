README
======

Hangman is a game based on guessing a hidden phrase/song/words.

Installation on Mac
--------------------

* Clone the repository:

```
mkdir -p $HOME/python_apps
cd $HOME/python_apps
git clone git@github.com:alok87/hangman
```

* Install Python, Flask :

```
http://docs.python-guide.org/en/latest/starting/install/osx/
sudo easy_install virtualenv
```

* Create a virtual environment with the requirments file

```
cd $HOME/python_apps/hangman
source flask/bin/activate
pip install -r requirements
```

* Start the application on the default port 5000

```
cd $HOME/python_apps/hangman
./run.py
```

* Browse the application at http://localhost:5000

