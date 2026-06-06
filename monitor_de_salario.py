''' O @property transforma um método (função) em um "atributo de leitura".

Em vez de chamar objeto.name() (com parênteses), você passa a chamar apenas objeto.name (sem parênteses). 
Por que usar isso?
Esconder o atributo real: O sublinhado em _name avisa que ele é "privado" e não deve ser mexido direto.

Segurança: Desse jeito, qualquer pessoa consegue ler o nome, mas não consegue alterá-lo (ex: objeto.name = "Novo Nome" vai dar erro, a menos que você crie um @name.setter).

Exatamente! O setter é o que dá a permissão para alterar o valor.

Em programação, "Getter" (pegar) e "Setter" (definir) são apenas nomes conceituais para as funções que controlam o acesso a um atributo. No Python, o @property é o cara que cria o getter.

# --- O GETTER ---
    @property
    def name(self):
        return self._name  # Devolve o valor quando você faz: print(p.name)

    # --- O SETTER ---
    @name.setter
    def name(self, valor):
        self._name = valor  # Altera o valor quando você faz: p.name = "Novo"
'''

