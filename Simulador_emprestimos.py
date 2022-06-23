import math

class Simulador_emprestimos:

    def __init__(self, valor_emprestimo_, tempo_pagamento_, taxa_juro_):
        self.valor_emprestimo = valor_emprestimo_
        self.tempo_pagamento = tempo_pagamento_
        self.taxa_juro = taxa_juro_
        self.valor_futuro = self.valor_emprestimo * (math.pow((1 + (self.taxa_juro / 100)), self.tempo_pagamento))

    def parcelas(self):
        valor_parcela = self.valor_futuro / self.tempo_pagamento
        return valor_parcela

    def juros(self):
        juro_efetivo = ((self.valor_futuro / self.valor_emprestimo) - 1) * 100
        return juro_efetivo