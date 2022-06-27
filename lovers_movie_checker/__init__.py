import asyncio

from loguru import logger as log

from .server import build_app, run_server
from .settings import Config
from . import db


log.remove(0)
log.add(
    '.\log\{time:DD-MM-YYYY}.log', 
    format='{time:HH:mm:ss.SSSZ} | [{level}] | {name}:{function}({line}) | {message}', 
    rotation="00:01", 
    retention="7 days", 
    compression="zip"
)


cfg = Config()
__version__ = (1, 0, 0, 0)

def run():
    try:
        log.debug(('='*25) + 'Lover\'s Movie Checker v' + ".".join(str(x) for x in __version__) + ('='*25))
        # Здесь можно запускать приложение
        asyncio.run(run_server(build_app()))
        
    except KeyboardInterrupt:
        log.debug('Штатное завершение программы...')
        return
    except Exception as e:
        log.error(f'Приложение завершилось с ошибкой ({e.__class__.__name__}) : {str(e)}')
