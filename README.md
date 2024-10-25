# drw-tetris

A simple Tetris simulator


## Build and Run

### Using Python Virtualenv

Setup 
```
$ python -m pip install --upgrade pip build setuptools wheel
```

Create virtualenv
```
$ cd drw-tetris
$ python -m venv .venv

# Activate environment with:
source .venv/bin/activate # on Unix/macOS
# or   
.venv\Scripts\activate # on Windows

$ python -m pip install -r requirements.txt
$ python -m pip install -e .
```

Create and install distribution
```
$ python -m build .
$ pip install dist/tetris-0.0.1-py3-none-any.whl
```

#### Run Simulator
```
$ python -m tetris < input.txt > output.txt
```

#### Run Unit Tests
```
$ python -m unittest discover -s tests
```

### Using Docker

Build image
```
$ docker build -t tetris .
```

Create container
```
$ docker run --name tetris -it -d tetris
```

#### Run Simulator
```
$ docker exec -i tetris python -m tetris < input.txt > output.txt
```


### Using Executable

Create executable

[Optional. Can use the pre-created executable `tetris.exe` in `/dist` instead]
```
$ pyinstaller --paths src/tetris --name tetris --onefile src/tetris/__main__.py
```

#### Run Simulator
```
$ ./dist/tetris < input.txt > output.txt
```