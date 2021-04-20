# google-calendar-tools

My tools for Google Calendar

## Setup

```
$ git git@github.com:tayutaedomo/google-calendar-tools.git
$ cd google-calendar-tools
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

### Lint and Formatter

```
$ pip install flake8
$ pip install autopep8
```

settings.json

```
{
  "editor.formatOnSave": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.lintOnSave": true,
  "python.formatting.provider": "autopep8"
}
```
