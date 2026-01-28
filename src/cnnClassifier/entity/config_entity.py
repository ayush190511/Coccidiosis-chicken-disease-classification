from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path                   # Type hint: This expects a Path object
    base_model_path: Path            # Where the generic model (e.g., VGG16) is saved
    updated_base_model_path: Path    # Where your custom model will be saved
    params_image_size: list          # [224, 224, 3]
    params_learning_rate: float      # 0.001
    params_include_top: bool         # False (transfer learning)
    params_weights: str              # 'imagenet'
    params_classes: int  


@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path