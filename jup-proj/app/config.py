from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    FALKOR_HOST: str = os.getenv("FALKOR_HOST")
    FALKOR_USERNAME: str = os.getenv("FALKOR_USERNAME")
    FALKOR_PASSWORD: str = os.getenv("FALKOR_PASSWORD")
    FALKOR_PORT: str = os.getenv("FALKOR_PORT")


settings = Settings()
