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
    #      `source .venv/bin/activate` on Unix/macOS
    # or   `.venv\Scripts\activate` on Windows

$ python -m pip install -r requirements.txt
$ python -m pip install --editable .
```

Create distribution
```
$ python -m build .
```

#### Run Simulator
```
$ python src/main.py < input.txt > output.txt
```

#### Run Unit Tests
```
$ python -m unittest discover -s tests
```

### Using Docker

Build image
```
$ docker build -t drw-tetris .
```

Create container
```
$ docker run --name drw-tetris -it -d drw-tetris
```

#### Run Simulator
```
$ docker exec -i drw-tetris python src/main.py < input.txt > output_local.txt
```


### Using Executable

Create executable

[Optional. Can use the pre-created executable `tetrix.exe` in `/dist` instead]
```
$ pyinstaller --paths src/tetris_engine --name tetris --onefile src/main.py
```

#### Run Simulator
```
$ ./dist/tetris < input.txt > output.txt
```