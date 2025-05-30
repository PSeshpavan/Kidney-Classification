import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from Kidney_Disease_Classsification.config.configuration import EvaluationConfig
from Kidney_Disease_Classsification.utils.common import save_json



class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
        
    def _valid_generator(self):
        
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.30
        )
        
        dataflow_kwargs = dict(
           target_size = self.config.params_image_size[:-1],
           batch_size = self.config.params_batch_size,
           interpolation = "bilinear"
        )
        
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        
        self._valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        ) 
        
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    
    def evaluate(self):
        self.model = self.load_model(self.config.path_to_model)
        self._valid_generator()
        self.score = self.model.evaluate(self._valid_generator)
        self.save_scores()
        
        
    def save_scores(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)
        
        
    def log_to_mlflow(self):
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}                
            )
            
            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="Kidney_Disease_Classsification USING VGG16 Model")
            else:
                mlflow.keras.log_model(self.model, "model")