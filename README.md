# eDoctor API

## Development environment Setup
Clone project and change directory to project folder

```
git clone https://github.com/joshua-mjjj/eDoctor_api.git
```

You can generate a secret key for your development environment by following the steps.
Start the interractive python shell and issue the commands below

```
python
>>>import binascii
>>>import os
>>>binascii.hexlify(os.urandom(24))
```

A random generated string will be produced. Copy without quotes and subsitute for
SECRET_KEY variable. E.g
```
b'f9ce7926e1b11a1f5e64c152a5a900f5335739224d073ce1'
```

Install requirements
```
pip install -r requirements.txt
```