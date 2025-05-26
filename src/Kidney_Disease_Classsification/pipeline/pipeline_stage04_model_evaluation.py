from Kidney_Disease_Classsification.config.configuration import ConfigurationManager
from Kidney_Disease_Classsification.components.model_evaluation_with_mlflow import Evaluation
from Kidney_Disease_Classsification import logger


STAGE_NAME = "Model Evaluation Stage"



class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluate()
        evaluation.log_to_mlflow()




if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        pipeline = ModelEvaluationPipeline()
        pipeline.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
        logger.info(f"*******************")
    except Exception as e:
        logger.exception(e)
        raise e