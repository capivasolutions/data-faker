import os
from dotenv import load_dotenv

load_dotenv()


class Environment:
    """
        Environment is the main access port to .env variables.
    """
    CREDIT_CARD_DATASET = os.getenv('CREDIT_CARD_DATASET')
