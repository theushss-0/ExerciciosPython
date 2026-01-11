from abc import ABC, abstractmethod
class Notificacao(ABC):

    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:...

class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool:
        print(f"E-mail: Enviando Mensagem...\nMensagem: {self.mensagem}")
        return True

class NotificacaoSMS(Notificacao):

    def enviar(self) -> bool:
        print(f"SMS: Enviando Mensagem...\nMensagem: {self.mensagem}")
        return True


def enviar_mensagem(notificacao: Notificacao): ## (paramentro: tipo_dado)nesse momento está acontecendo o polimorfismo
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("Notificação enviada!")

    else:
        print("Notificação NÃO enviada!")


# tipos que herdam de Notificacao também pode ser passado como parâmetro assinado como Notificacao
mensagem_email = NotificacaoEmail("Estou enviando este email para vocês") # NotificaoEmail, herda de notificacao
mensagem_sms= NotificacaoSMS("Estou enviando este SMS para você") # NotificaoSMS, herda de notificacao

enviar_mensagem(mensagem_email)
enviar_mensagem(mensagem_sms)

