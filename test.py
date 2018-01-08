n = 10
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')


import pyipinfodb
ip_lookup = pyipinfodb.IPInfo('877d192cdb8b0543b679dd6e5c2bd6e48c55016aaf6844f6495f1f7772b801d4')
ip_lookup.get_country('8.8.8.8')

from requests import get
loc = get('https://ipapi.co/json/').text
print(loc)

import socket
socket.gethostbyname(socket.gethostname())

g = "Golf"
h = "Hotel"
print('% and %') % (g, h)



