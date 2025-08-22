# merging all the steps
from config.paths_config import *
from utils.common_functions import read_yaml
from src.data_ingestion import DataIngestion
from src.data_processing import DataProcessor
from src.model_training import ModelTraining


if __name__ =="__main__":
    # data_ingestion = Data_Ingestion(read_yaml(CONFIG_PATH))
    # data_ingestion.run()
    # no need for data_ingestion here, we already have our data downloaded/ ingested from gcp
    #  all the files in our artifacts folder will be pushed to another GCP bucket
    # so will extract those data from DVC

    data_processor = DataProcessor(ANIMELIST_CSV, PROCESSED_DIR)
    data_processor.run()

    model_trainer = ModelTraining(PROCESSED_DIR)
    model_trainer.train_model()

