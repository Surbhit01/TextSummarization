from textSummarization.logging import logger
from textSummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STATE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>state {STATE_NAME} started<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>state {STATE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
