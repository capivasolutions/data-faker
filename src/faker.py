import pandas as pd
from pandas import DataFrame
from imblearn.over_sampling import BorderlineSMOTE
from config import Logger, Environment


class Faker:
    """
        Faker can generate fake transactions based on input dataset.
        It uses oversampling to generate new fraudulent transactions.
    """

    def __init__(self) -> None:
        self.data = None
        self.rebalanced_data = None
        self.k_neighbors = 3
        self.m_neighbors = 2
        self.sampling_strategy = 'minority'
        self.logger = Logger.get_instance()
        self.__init()

    def __init(self) -> None:
        self.__read_dataset()
        self.__rebalanced_dataset()

    def __read_dataset(self) -> None:
        self.logger.debug('Loading dataset from disk')
        self.data = pd.read_csv(Environment.CREDIT_CARD_DATASET, sep=',')
        self.logger.debug('Dataset loaded from disk')

    def __rebalanced_dataset(self) -> None:
        self.logger.debug('Applying oversampling to dataset')
        smote_attributes = self.data.drop('Class', axis=1)
        smote_class = self.data['Class']

        smote = BorderlineSMOTE(k_neighbors=self.k_neighbors,
                                m_neighbors=self.m_neighbors,
                                sampling_strategy=self.sampling_strategy)
        x_smote, y_smote = smote.fit_resample(smote_attributes, smote_class)

        self.rebalanced_data = pd.DataFrame(x_smote, columns=self.data.columns)
        self.rebalanced_data['Class'] = y_smote
        self.logger.debug(
            f'Oversampling applied to dataset. {len(self.rebalanced_data)} transactions')

    def generate_transaction(self) -> DataFrame:
        self.logger.debug('Finding a random transaction from dataset')
        random_transaction = self.rebalanced_data.sample(n=1)
        self.rebalanced_data = self.rebalanced_data.drop(
            random_transaction.index)
        self.logger.debug(
            f'{len(self.rebalanced_data)} transactions remaining')
        self.logger.debug(f'Random transaction details:\n{random_transaction}')
        return random_transaction
