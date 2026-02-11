from sqlalchemy import create_engine, text

from src.core.config import settings 

def main():
    engine = create_engine(settings.database_url, pool_pre_ping=True)

    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Conexão OK, SELECT 1 =", result.scalar())

if __name__ == "__main__":
    main()
