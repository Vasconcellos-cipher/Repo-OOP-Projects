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

try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    catalogue.add(movie1)
    series1 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    catalogue.add(series1)
except (ValueError, MediaError) as e:
    pass

# Main Menu Loop
while True:
    print("\n" + "="*30)
    print("      CATALOGUE MENU")
    print("="*30)
    print("[ 1 ] Add New Movie")
    print("[ 2 ] Add New TV Series")
    print("[ 3 ] Display Full Catalogue")
    print("[ 4 ] Exit Program")
    print("="*30)
    
    option = input("Choose an option: ").strip()
    
    if option == '1':
        print("\n--- ADD NEW MOVIE ---")
        try:
            user_title = input("Enter movie title: ")
            user_year = int(input("Enter release year: "))
            user_director = input("Enter director's name: ")
            user_duration = int(input("Enter duration in minutes: "))
            
            new_movie = Movie(user_title, user_year, user_director, user_duration)
            catalogue.add(new_movie)
            print("\n✅ Movie added successfully!")
            
        except ValueError as e:
            print(f'\n❌ Validation Error: {e}. The movie was not added.')
        except MediaError as e:
            print(f'\n❌ Catalogue Error: {e}')
            
    elif option == '2':
        print("\n--- ADD NEW TV SERIES ---")
        try:
            user_title = input("Enter TV series title: ")
            user_year = int(input("Enter release year: "))
            user_director = input("Enter director/creator's name: ")
            user_duration = int(input("Enter average episode duration (min): "))
            user_seasons = int(input("Enter number of seasons: "))
            user_episodes = int(input("Enter total number of episodes: "))
            
            # Create and add the series using the TVSeries class
            new_series = TVSeries(user_title, user_year, user_director, user_duration, user_seasons, user_episodes)
            catalogue.add(new_series)
            print("\n✅ TV Series added successfully!")
            
        except ValueError as e:
            print(f'\n❌ Validation Error: {e}. The TV series was not added.')
        except MediaError as e:
            print(f'\n❌ Catalogue Error: {e}')
        
    elif option == '3':
        print("\n" + "-"*40)
        print(catalogue)
        print("-"*40)
        
    elif option == '4':
        print("\nExiting the system... See you later! 👋")
        break
        
    else:
        print("\n⚠️ Invalid option! Please enter 1, 2, 3, or 4.")