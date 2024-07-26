from datetime import datetime
import os

AWS_S3_BUCKET_NAME = "sensordeployment1"
#artifacts folder will be stored in this bucket
MONGO_DATA_BASE_NAME = "cluster0"

TARGET_COLUMN = "Result"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder_name = datetime.now().strftime("%m_%d_%Y_%H_%M_S")
artifact_folder = os.path.join("artifacts",artifact_folder_name)