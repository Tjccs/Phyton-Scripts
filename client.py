import requests
import sys

sys.stdout.write(str('EXIT') + '\n')
while True:
    #    sys.stdout.write(str('Write EXIT to close the terminal') + '\n')
    if sys.argv[1] == 'ADD':
        if sys.argv[2] == 'USER':
            try:
                data = {'nome' : sys.argv[3], 'username' : sys.argv[4], 'password' : sys.argv[5]}
                r = requests.post('http://localhost:5000/utilizadores/add', json=data)
                r.raise_for_status()
                print('USER ADDED')
                print(r.status_code)
                print(r.text)
                break
            except:
                print(r.json)
        if sys.argv[2] == 'BANDA':
            try:
                r = requests.post('http://localhost:5000/bandas/add', data)
            except:
                print(r.json)
        if sys.argv[2] == 'ALBUM':
            try:
                r = requests.post('http://localhost:5000/albuns/add', data)
            except:
                print(r.json)
        if sys.argv[2].isdigit():
            try:
                r = requests.post('http://localhost:5000/', data)
            except:
                print(r.json)

    if sys.argv[1] == 'REMOVE':
        if sys.argv[2] == 'USER':
            try:
                r = requests.delete('http://localhost:5000/utilizadores/delete', data)
            except:
                print(r.json)
        if sys.argv[2] == 'BANDA':
            try:
                r = requests.delete('http://localhost:5000/bandas/delete', data)
            except:
                print(r.json)
        if sys.argv[2] == 'ALBUM':
            r = requests.delete('http://localhost:5000/albuns/delete', data)
            if r.raise_for_status():
                print(r.json)
        if sys.argv[2] == 'ALL':
            if sys.argv[3] == 'USERS':
                r = requests.delete('http://localhost:5000/utilizadores/delete_all', data)
            if sys.argv[3] == 'BANDAS':
                r = requests.delete('http://localhost:5000/bandas/delete_all', data)
            if sys.argv[3] == 'ALBUMS':
                r = requests.delete('http://localhost:5000/albuns/delete_all', data)
            if sys.argv[3] == 'ALBUMS_B':
                r = requests.delete('http://localhost:5000/albuns/delete_all', data)
            if sys.argv[3] == 'ALBUMS_U':
                r = requests.delete('http://localhost:5000/albuns/delete_all', data)

    if sys.argv[1] == 'SHOW':
        print('SHOW')

    if sys.argv[1] == 'UPDATE':
        if sys.argv[2] == 'ALBUM':
            pass
        if sys.argv[2] == 'USER':
            pass

    if sys.argv[1] == 'EXIT':
        print('Exiting...')
        sys.exit()
