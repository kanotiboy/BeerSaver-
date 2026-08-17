import os

class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://beersaver:beersaver_password@localhost:5432/beersaver"
    )

    JWT_SECRET: str = os.getenv("JWT_SECRET", "supersecretjwt")

settings = Settings()
