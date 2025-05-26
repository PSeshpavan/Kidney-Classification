from Kidney_Disease_Classsification.config.configuration import ConfigurationManager
from Kidney_Disease_Classsification.components.model_training import Training
from Kidney_Disease_Classsification import logger


STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        
if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        pipeline = ModelTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
        logger.info(f"*******************")
    except Exception as e:
        logger.exception(e)
        raise e