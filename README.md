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

### Start a Juptyer Notebook
*Assuming pip libraries are installed*
```bash
$ juptyer notebook
```
    The browser will open. And you will see the working directory.
    Click New -> Python3 
    Enjoy :)

### Run the Flask App in Dev mode
```bash
$ export FLASK_APP=src/main/flaskr
$ export FLASK_ENV=development
```
