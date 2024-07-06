from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValiadtion
from mlProject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_valiation=DataValiadtion(config=data_validation_config)
        data_valiation.validate_all_columns()

if __name__=="__main__":
    try:
        logger.info(f">>>> {STAGE_NAME} Started <<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>> {STAGE_NAME} Completed <<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e