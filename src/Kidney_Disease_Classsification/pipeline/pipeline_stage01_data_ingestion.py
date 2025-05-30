from Kidney_Disease_Classsification.config.configuration import ConfigurationManager
from Kidney_Disease_Classsification.components.data_ingestion import DataIngestion
from Kidney_Disease_Classsification import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()
        
if __name__ == "__main__":
    try:
        logger.info("*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
        logger.info("*******************")
    except Exception as e:
        logger.exception(e)
        raise e

