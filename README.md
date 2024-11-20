# py-tetris

A simple Tetris simulator


## Building and Running
* [Using Python virtualenv](#if-using-python-virtualenv)
    * [Windows (Git Bash)](#windows-git-bash)
        * [Running Simulator](#running-simulator)
        * [Running Unit Tests](#running-unit-tests)
    * [Linux (Ubuntu-24 LTS)](#linux-ubuntu-24-lts)
        * [Running Simulator](#running-simulator-1)
        * [Running Unit Tests](#running-unit-tests-1)
* [Using Docker](#if-using-docker)
    * [Running Simulator](#running-simulator-2)
* [Using Executable](#if-using-executable)
    * [Running Simulator](#running-simulator-3)


### If using Python virtualenv

#### Windows (Git Bash)

Setup 
```
$ python -m pip install --upgrade pip build setuptools wheel
```

Create virtualenv
```
$ cd drw-tetris
$ python -m venv .venv

# Activate environment
source .venv/Scripts/activate

$ python -m pip install -r requirements.txt
$ python -m pip install -e .
```

##### Running Simulator
```
$ python -m tetris < input.txt > output.txt
```

##### Running Unit Tests
```
$ python -m unittest discover -s tests
```

#### Linux (Ubuntu-24 LTS)

Setup 
```
$ sudo apt install python3-pip python3-setuptools python3-build python3-wheel python3-venv
```

Create virtualenv
```
$ cd drw-tetris
$ python3 -m venv .venv

# Activate environment
source .venv/bin/activate

$ python3 -m pip install -r requirements.txt
$ python3 -m pip install -e .
```

##### Running Simulator
```
$ python3 -m tetris < input.txt > output.txt
```

##### Running Unit Tests
```
$ python3 -m unittest discover -s tests
```



### If using Docker

Build image
```
$ docker build -t tetris .
```

Create container
```
$ docker run --name tetris -it -d tetris
```

#### Running Simulator
```
$ docker exec -i tetris python -m tetris < input.txt > output.txt
```


### If using Executable

Create executable

[Optional. Can use the pre-created executable `tetris.exe` in `/dist` instead]
```
$ pyinstaller --paths src/tetris --name tetris --onefile src/tetris/__main__.py
```

#### Running Simulator
```
$ ./dist/tetris < input.txt > output.txt
```
