from src.Sentimentanalysis.logging import logger
from src.Sentimentanalysis.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.Sentimentanalysis.pipeline.stage_01 import DataValidationPipeline

#STAGE_NAME = "Data Ingestion stage"
#try:
#   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#   obj=DataIngestion()
#   train_data,test_data=obj.initiate_data_ingestion()
#   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#except Exception as e:
#        logger.exception(e)
#        raise e

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation=DataValidationPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

