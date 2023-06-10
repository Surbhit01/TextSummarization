from textSummarization.logging import logger
from textSummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarization.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarization.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarization.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarization.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STATE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>state {STATE_NAME} started<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>state {STATE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STATE_NAME = "Data Validation"
try:
    logger.info(f">>>>>state {STATE_NAME} started<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>state {STATE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STATE_NAME = "Data Transformation"
try:
    logger.info(f">>>>>state {STATE_NAME} started<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>state {STATE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STATE_NAME = "Model Trainer"
try:
    logger.info(f">>>>>state {STATE_NAME} started<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>state {STATE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STATE_NAME = "Model Evaluation"
try:
    logger.info(f">>>>>state {STATE_NAME} started<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>state {STATE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e