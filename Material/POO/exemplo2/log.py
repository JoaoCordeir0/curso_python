from pathlib import Path

FILE_LOG = Path(__file__).parent / 'log.txt'

# Abstração
class Log:
    # Assinatura do método
    def _log(self, msg): 
        raise NotImplementedError('Implemente o método log')    
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):        
        msg = f'{msg} ({self.__class__.__name__})'
        print(f'Salvando no log: {msg}')
        with open(FILE_LOG, 'a') as file:
            file.write(msg)
            file.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

 