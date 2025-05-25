from Kidney_Disease_Classsification.components.base_model import PrepareBaseModel
from Kidney_Disease_Classsification.config.configuration import ConfigurationManager
from Kidney_Disease_Classsification import logger


STAGE_NAME = "Prepare Base Model"


class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info("*******************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        prepare_base_model_pipeline = PrepareBaseModelPipeline()
        prepare_base_model_pipeline.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
        logger.info("*******************")
    except Exception as e:
        logger.exception(e)
        raise e