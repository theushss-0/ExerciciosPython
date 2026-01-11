from pathlib import Path
from abc import ABC, abstractmethod

LOG_FILE = Path(__file__).parent / "log.txt"


class Log(ABC):
    @abstractmethod
    def _log(self,msg): ...
    
    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_success(self, msg):
        return self._log(f"Sucess: {msg}")

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f"{msg} ({self.__class__.__name__})"
        try:
            with open(LOG_FILE, "a", encoding='utf8') as arquivo:
                arquivo.write(msg_formatada)
                arquivo.write("\n")
        except:
            with open(LOG_FILE, "w", encoding='utf8') as arquivo:
                arquivo.write(msg_formatada)
                arquivo.write("\n")

        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        msg_formatada = f"{msg} ({self.__class__.__name__})"
        try:
            with open(LOG_FILE, "a", encoding='utf8') as arquivo:
                arquivo.write(msg_formatada)
                arquivo.write("\n")
        except:
            with open(LOG_FILE, "w", encoding='utf8') as arquivo:
                arquivo.write(msg_formatada)
                arquivo.write("\n")
        print(msg)


if __name__ ==  "__main__":
    lf = LogFileMixin()

#    lf.log_error("Mensagem de erro!")
#    lf.log_error("Mensagem de sucess!")

    lp = LogPrintMixin()

#    lp.log_success("Mensagem de erro!")
#    lp.log_success("Mensagem de sucess!")

    #log = Log() # Não pode implementar uma classe abstrata

    #log.log_error("Olá") #não pode usar o metodo de uma classe abstrada