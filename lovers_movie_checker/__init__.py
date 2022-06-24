
__version__ = (1, 0, 0, 0)

def run():
    try:
        print(('='*25) + 'Lover\'s Movie Checker v' + ".".join(str(x) for x in __version__) + ('='*25))
        
    except KeyboardInterrupt:
        print('Штатное завершение программы...')