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
    "python.linting.flake8Args": [
    "--ignore=E111, E114, E402, E501"
  ],
  "python.linting.lintOnSave": true,
  "python.formatting.provider": "autopep8",
    "python.formatting.autopep8Args": [
    "--indent-size=2",
    "--ignore E402"
  ]
}
```

## Scripts

```
$ python scripts/quickstart.py
$ python scripts/calendar_list.py
$ python scripts/event_list.py "Calendar ID" "2021-04-01T00:00:00Z" "2021-05-01T00:00:00Z"
$ python scripts/events_to_csv.py "Calendar ID" "2021-04-01T00:00:00+0900" "2021-05-01T00:00:00+0900" "keyword"
```
