class MediaError(Exception):
    """Custom exception for media-related errors."""

    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj

class Movie:
    """Parent class representing a movie."""
    
    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not director.strip():
            raise ValueError('Director cannot be empty')
        if duration <= 0:
            raise ValueError('Duration must be positive')
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'

class TVSeries(Movie):
    """Child class representing an entire TV series."""

    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)

        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        
        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'

class MediaCatalogue:
    """A catalogue that can store different types of media items."""

    def __init__(self):
        self.items = []

    def add(self, media_item):
        if not isinstance(media_item, Movie):
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        self.items.append(media_item)

    def get_movies(self):
        return [item for item in self.items if type(item) is Movie]

    def get_tv_series(self):
        return [item for item in self.items if isinstance(item, TVSeries)]
    
    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        
        movies = self.get_movies()
        series = self.get_tv_series()

        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        if movies:
            result += '=== MOVIES ===\n'
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'
        if series:
            result += '\n=== TV SERIES ===\n'
            for i, serie in enumerate(series, 1):
                result += f'{i}. {serie}\n'
        return result

# --- SISTEMA INTERATIVO DO CATÁLOGO ---

catalogue = MediaCatalogue()

# Itens iniciais inseridos automaticamente (opcional)
try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    catalogue.add(movie1)
    series1 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    catalogue.add(series1)
except (ValueError, MediaError) as e:
    pass

# Loop principal do Menu
while True:
    print("\n" + "="*30)
    print("      MENU DO CATÁLOGO")
    print("="*30)
    print("[ 1 ] Cadastrar novo Filme")
    print("[ 2 ] Cadastrar nova Série")
    print("[ 3 ] Exibir Catálogo Completo")
    print("[ 4 ] Sair do Programa")
    print("="*30)
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        print("\n--- CADASTRO DE NOVO FILME ---")
        try:
            user_title = input("Digite o título do filme: ")
            user_year = int(input("Digite o ano de lançamento: "))
            user_director = input("Digite o nome do diretor: ")
            user_duration = int(input("Digite a duração em minutos: "))
            
            novo_filme = Movie(user_title, user_year, user_director, user_duration)
            catalogue.add(novo_filme)
            print("\n✅ Filme adicionado com sucesso!")
            
        except ValueError as e:
            print(f'\n❌ Erro de Validação: {e}. O filme não foi adicionado.')
        except MediaError as e:
            print(f'\n❌ Erro no Catálogo: {e}')
            
    elif opcao == '2':
        print("\n--- CADASTRO DE NOVA SÉRIE ---")
        try:
            user_title = input("Digite o título da série: ")
            user_year = int(input("Digite o ano de lançamento: "))
            user_director = input("Digite o nome do diretor/criador: ")
            user_duration = int(input("Digite a duração média dos episódios (min): "))
            user_seasons = int(input("Digite a quantidade de temporadas: "))
            user_episodes = int(input("Digite o total de episódios: "))
            
            # Cria e adiciona a série usando a classe TVSeries
            nova_serie = TVSeries(user_title, user_year, user_director, user_duration, user_seasons, user_episodes)
            catalogue.add(nova_serie)
            print("\n✅ Série adicionada com sucesso!")
            
        except ValueError as e:
            print(f'\n❌ Erro de Validação: {e}. A série não foi adicionada.')
        except MediaError as e:
            print(f'\n❌ Erro no Catálogo: {e}')
        
    elif opcao == '3':
        print("\n" + "-"*40)
        print(catalogue)
        print("-"*40)
        
    elif opcao == '4':
        print("\nEncerrando o sistema... Até logo! 👋")
        break
        
    else:
        print("\n⚠️ Opção inválida! Digite 1, 2, 3 ou 4.")
