Dumb midi utilities'n'stuff
===========================

Dumb and simple midi stuff to mess around with. Primarly python.
Depends on rtmidi.

Feels free to hack this stuff

Recommended bootstrap procedure :
```bash
virtualenv --python=python3.7 env
source ./env/bin/activate
pip install -r requirements.txt
```

To launch an example script :
```bash
PYTHONPATH=$PYTHONPATH:$(pwd)/lib ./env/bin/python3.7 -m examples.<example_name>
```
