from log import LogFileMixin, LogPrintMixin

from eletronico import Smartphone

#lp = LogPrintMixin()
#lp.log_error('Error')
#lp.log_success('Sucesso')

lf = LogFileMixin()
lf.log_error('Error')
lf.log_success('Sucesso')

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('Iphone')

galaxy_s.ligar()
iphone.desligar()
