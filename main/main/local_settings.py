from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
text = 'SECRET_KEY = \'{0}\''.format(secret_key)
print(text)

SECRET_KEY = '9l%j$12+)#0ij(6#gm1-xv(7k303fqb70u4k^dys388z#97-+z'