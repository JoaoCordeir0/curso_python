# from log import LogFileMixin, LogPrintMixin

# lp = LogPrintMixin()
# lp.log_error('Qualquer coisa')
# lp.log_success('Top')
    
# lf = LogFileMixin()
# lf.log_error('Qualquer coisa')
# lf.log_success('Que legal')   

from eletronico import Smartphone

galaxys22 = Smartphone('Galaxy S22')
iphone15 = Smartphone('Iphone 15')

galaxys22.ligar()
iphone15.desligar()