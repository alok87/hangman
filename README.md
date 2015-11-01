README
======

Hangman is a game based on guessing a hidden phrase/song/words.

Installation on Mac
--------------------

* Clone the repository:

```
mkdir -p $HOME/pythonApps
cd $HOME/pythonApps
git clone git@github.com:alok87/hangman
```

* Install Python, Flask :

```
http://docs.python-guide.org/en/latest/starting/install/osx/
sudo easy_install virtualenv
```

* Create a virtual environment with the requirments file

```
cd $HOME/pythonApps/hangman
source flask/bin/activate
pip install -r requirements
```

* Start the application on the default port 5000

```
cd $HOME/pythonApps/hangman
./run.py
```

* Browse the application at http://localhost:5000

