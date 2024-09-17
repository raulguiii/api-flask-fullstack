import sqlite3

def init_db():
    # Conecta ao banco de dados (ou cria um novo se não existir)
    with sqlite3.connect('database.db') as conn:
        # Abre o arquivo schema.sql e executa o script SQL
        with open('schema.sql') as f:
            conn.executescript(f.read())

if __name__ == "__main__":
    init_db()
