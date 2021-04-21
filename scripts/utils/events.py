from utils.api import fetch_events


class Events:
  def __init__(self):
    self.items = []

  def fetch(self, params):
    events = fetch_events(params)
    self.items = events['items']
    return self.items

  def to_csv(self, filename):
    for obj in self.items:
      item = EventItem(obj)

      csv_line = '"{}","{}","{}","{}"'.format(
          item.get_summary(),
          '1' if item.is_all_day() else '0',
          item.get_start(),
          item.get_end()
      )

      with open(filename, 'a') as f:
          f.write(csv_line + '\n')


class EventItem:
  def __init__(self, item):
    self.item = item

  def get_summary(self):
    return self.item.get('summary')

  def get_start(self):
    d = self.get_start_date()
    if d != '':
      return d

    return self.get_start_datetime()

  def get_start_date(self):
    start = self.item.get('start')

    if not start:
      return ''

    d = start.get('date')
    if d:
      return d

    return ''

  def get_start_datetime(self):
    start = self.item.get('start')

    if not start:
      return ''

    dt = start.get('dateTime')
    if dt:
      return dt

    return ''

  def is_all_day(self):
    return self.get_start_date() != ''

  def get_end(self):
    d = self.get_end_date()
    if d != '':
      return d

    return self.get_end_datetime()

  def get_end_date(self):
    end = self.item.get('end')

    if not end:
      return ''

    d = end.get('date')
    if d:
      return d

    return ''

  def get_end_datetime(self):
    end = self.item.get('end')

    if not end:
      return ''

    dt = end.get('dateTime')
    if dt:
      return dt

    return ''
