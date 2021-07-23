# This is a sample Python script.

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from app import create_app

app = create_app()

if __name__ == '__main__':
    try:
        app.debug = True
        app.run(use_reloader=False, host='127.0.0.1', port=7799)
    except:
        print('error')
