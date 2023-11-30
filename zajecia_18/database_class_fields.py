class DatabaseConnection:
    # Zmienna klasowa przechowująca ustawienia połączenia do bazy danych
    connection_settings = {
        'host': 'localhost',
        'port': 5432,
        'username': 'admin',
        'password': 'password123'
    }

    def __init__(self, database_name):
        self.database_name = database_name
        self.connection_settings_2_0 = {
        'host': 'localhost',
        'port': 5432,
        'username': 'admin',
        'password': 'password123'
        }

    def connect(self):
        # Tutaj używamy zmiennych klasowych do uzyskania ustawień połączenia
        print(f"Connecting to {self.database_name} database at {DatabaseConnection.connection_settings['host']}:{DatabaseConnection.connection_settings['port']}")

# Utwórz kilka instancji klasy DatabaseConnection
db1 = DatabaseConnection("CustomerDB")
db2 = DatabaseConnection("ProductDB")

# Wywołaj metodę connect dla każdej instancji
db1.connect()
db2.connect()

