#class A:
#    def funcao_abs(self):
#        raise NotImplementedError("Implemente essa função")
#    

#class B(A):
#    def funcao_abs(self):
#        print("função implementada")
    


#absFunc = B()

#absFunc.funcao_abs()


class Log:

    def _log(self,msg):
        raise NotImplementedError("Implemente a Classe")
    
    def log_error(self, msg):
        return self._log(f"Error: {msg}")
    
    def log_success(self, msg):
        return self._log(f"Sucess: {msg}")
    

class LogFileMixin(Log):

    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log):

    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")



if __name__ == '__main__':

    fileLog = LogFileMixin()
    printLog = LogPrintMixin()

    fileLog.log_success("Função Implementada!!")
    printLog.log_error("Ops temos um problema aqui!!")