from config import Logger, Environment
import requests


class Service:
    def __init__(self) -> None:
        self.logger = Logger.get_instance()

    def send_transaction(self, transaction_dataframe) -> None:
        try:
            transaction = transaction_dataframe.to_dict('records')[0]
            transaction = {k.lower(): v for k, v in transaction.items()}
            del transaction['class']
            url = Environment.BACK_END_URL + '/transactions'
            requests.post(url=url, json=transaction)
        except Exception as error:
            self.logger.error(error, 'Error while sending transaction')
