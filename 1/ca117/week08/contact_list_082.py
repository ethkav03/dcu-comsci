class Contact(object):
  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email

  def __str__(self):
    return '{} {} {}'.format(self.name, self.phone, self.email)

class ContactList(object):
  def __init__(self, d=None):
    self.d = {} if d is None else d

  def add(self, contact):
    self.d[contact.name] = contact

  def remove(self, name):
    if name in self.d:
      del self.d[name]

  def get(self, name):
    if name in self.d:
      return self.d[name]
    else:
      return None

  def __str__(self):
    contacts = []
    contacts.append('Contact list')
    contacts.append('------------')
    for k, v in sorted(self.d.items()):
      contacts.append('{}'.format(v))
    return '{}'.format('\n'.join(contacts))
