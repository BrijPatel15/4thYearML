# Python Core

## How - To

### Install virtualenv
*Must have python 3.7 or higher*

```bash
$ pip install virtualenv
$ virtualenv mypythonenv #put any name python-core is recommended
```
### Activate virtualenv
*MacOS / Linux*
```bash
$ source mypython/bin/activate
```
*Windows*
```bash
$ mypthon\Scripts\activate
```

### Deactivate vitrualenv

```bash
$ deactivate
```
### Install libraries
*While inside the virtual environment*
```bash
$ pip install -r requirements.txt
```

### Add to requirements.txt
*While inside the virtual environment*
```bash
$ pip install ${your-packacge}
$ pip freeze > requirements.txt
```
