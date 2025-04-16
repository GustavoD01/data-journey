class PrecoDia:
    def __init__(self, dia):
        self.dia = dia.lower().strip()

    def obter_preco(self):
        dias_semana = ['segunda', 'terça', 'quarta', 'quinta']
        dias_fim_de_semana = ['sexta', 'sábado', 'domingo']

        if self.dia in dias_semana:
            return 20
        elif self.dia in dias_fim_de_semana:
            return 30
        else:
            raise ValueError("Dia inválido. Use nomes como 'segunda','terça' e etc")
        
cliente = 'José'
tipo = 'corte de cabelo'
horario = '16:45'
dia = 'sext'

try:
    preco = PrecoDia(dia).obter_preco()

    print("=== Agendamento ===")
    print(f"Cliente: {cliente}")
    print(f"Serviço: {tipo}")
    print(f"Horário: {horario}")
    print(f"Dia: {dia.capitalize()}")
    print(f"Valor: R${preco},00")
except ValueError as erro:
    print(f"Erro: {erro}")