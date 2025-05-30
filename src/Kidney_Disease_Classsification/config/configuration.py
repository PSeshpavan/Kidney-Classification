from Kidney_Disease_Classsification.constants import *
from Kidney_Disease_Classsification.utils.common import read_yaml, create_directories
from Kidney_Disease_Classsification.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, TrainingConfig, EvaluationConfig
import os

class ConfigurationManager:
    def __init__(self, config_file_path:str = CONFIG_FILE_PATH, params_file_path:str = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.model
        
        create_directories([config.root_dir])
        
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )
        
        return prepare_base_model_config

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        base_model = self.config.model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone")
        create_directories([
            Path(training.root_dir)
        ])
        
        
        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )
        
        return training_config
    
    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_to_model="artifacts/training/trained_model.keras",
            training_data="artifacts/data_ingestion/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone",
            all_params=self.params,
            mlflow_uri="https://dagshub.com/PSeshpavan/Kidney-Classification.mlflow",
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        
        return eval_config