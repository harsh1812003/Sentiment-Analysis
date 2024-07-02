from src.Sentimentanalysis.logging import logger
from src.Sentimentanalysis.conponents.data_ingestion import DataIngestion, DataIngestionConfig

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   obj=DataIngestion()
   train_data,test_data=obj.initiate_data_ingestion()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e