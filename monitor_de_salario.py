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

# Criamos uma "forma" ou "molde" chamada Employee (Empregado).
class Employee:
    
    # Isso é um dicionário da CLASSE. É uma tabela fixa de salários que todo mundo compartilha.
    # O underline antes (_base_salaries) é um aviso para outros programadores: "Não mexa aqui direto!".
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    # O construtor. É o que roda AUTOMATICAMENTE quando criamos um funcionário novo.
    def __init__(self, name, level):
        self.name = name    # Salva o nome (mas passa pelo "filtro" que criamos lá embaixo)
        self.level = level  # Salva o nível (também passa pelo "filtro" lá embaixo)
        
        # Define o salário inicial buscando direto na tabela lá de cima, usando o nível escolhido.
        self.salary = Employee._base_salaries[level]

    # Controla o que aparece se você der um "print(charlie_brown)". Mostra algo bonito para humanos.
    def __str__(self):
        return f'{self.name}: {self.level}'

    # Controla o que aparece se você olhar o objeto no console do Python. 
    # Mostra exatamente o comando que recriaria esse objeto.
    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

    # --- SEÇÃO DO NOME (NAME) ---

    # O @property transforma um método em uma "propriedade". 
    # Significa que podemos ler o nome usando 'objeto.name' (sem os parênteses de função).
    @property
    def name(self):
        return self._name   # Devolve o nome real que está escondido em _name.

    # O @name.setter é o "filtro/segurança" do nome. 
    # Toda vez que alguém tentar fazer 'objeto.name = "Novo Nome"', esse código roda primeiro.
    @name.setter
    def name(self, new_name):
        # Validação: Se o novo nome não for um texto (string), o Python trava e dá erro.
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        
        # Se passou no teste, salva o nome de verdade na variável escondida _name.
        self._name = new_name
        # Avisa na tela que o nome mudou.
        print(f"'name' updated to '{self.name}'.")

    # --- SEÇÃO DO NÍVEL (LEVEL) ---

    # Permite ler o nível atual fazendo apenas 'objeto.level'.
    @property
    def level(self):
        return self._level  # Devolve o nível real escondido em _level.

    # O "segurança" do nível. Protege contra cargos inventados ou rebaixamentos ilegais.
    @level.setter
    def level(self, new_level):
        # Regra 1: O cargo tem que ser um texto.
        if not isinstance(new_level, str):
            raise TypeError("'level' must be a string.")
        
        # Regra 2: O cargo tem que existir naquela tabela lá de cima (_base_salaries).
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        
        # Regra 3: Se a pessoa já tem um nível e tentar mudar para o MESMO nível, dá erro.
        if hasattr(self, '_level') and new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        
        # Regra 4: Não aceitamos rebaixamento! Se o salário do novo cargo for MENOR que o atual, dá erro.
        if hasattr(self, '_level') and Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError("Cannot change to lower level.")
        
        # Se passou por todas as regras:
        print(f"'{self.name}' promoted to '{new_level}'.") # Avisa da promoção!
        self.salary = Employee._base_salaries[new_level]   # Atualiza o salário pro mínimo do novo cargo.
        self._level = new_level                            # Salva o novo cargo na variável escondida.

    # --- SEÇÃO DO SALÁRIO (SALARY) ---

    # Permite ler o salário fazendo apenas 'objeto.salary'.
    @property
    def salary(self):
        return self._salary

    # O "segurança" do salário. Não deixa pagar menos que o mínimo do cargo.
    @salary.setter
    def salary(self, new_salary):
        # Regra 1: Salário tem que ser número inteiro ou quebrado (float).
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        
        # Regra 2: O novo salário não pode ser menor que o piso salarial do cargo atual dele.
        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(f'Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.')
        
        # Se passou no teste, atualiza o valor.
        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')


# --- TESTANDO O CÓDIGO NA PRÁTICA ---

# Criamos o objeto do Charlie Brown como 'trainee'.
# Isso vai disparar os filtros de Nome, Nível e Salário automaticamente!
charlie_brown = Employee('Charlie Brown', 'trainee')

# Vai usar o método __str__ para mostrar: "Charlie Brown: trainee"
print(charlie_brown)

# Vai ler a propriedade salary e mostrar: "Base salary: $1000"
print(f'Base salary: ${charlie_brown.salary}')

# Tentamos mudar o nível para 'junior'. 
# O filtro vai ver que 'junior' é maior que 'trainee' (R$ 2000 > R$ 1000), vai aceitar,
# vai atualizar o salário dele para 2000 e printar a promoção na tela!
charlie_brown.level = 'junior'