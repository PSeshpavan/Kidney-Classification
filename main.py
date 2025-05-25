from Kidney_Disease_Classsification import logger
from Kidney_Disease_Classsification.pipeline.pipeline_stage01_data_ingestion import DataIngestionPipeline
from Kidney_Disease_Classsification.pipeline.pipeline_stage02_base_model import PrepareBaseModelPipeline



STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("*******************")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("*******************")
except Exception as e:
    logger.exception(e)
    raise e