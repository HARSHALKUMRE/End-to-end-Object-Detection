import sys
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.pipeline.training_pipeline import TrainPipeline


try:
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()
except Exception as e:
    raise SignException(e, sys) from e
