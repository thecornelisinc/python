# import os
# def lambda_handler(event, context):
#     print('## ENVIRONMENT VARIABLES')
#     print(os.environ['AWS_LAMBDA_LOG_GROUP_NAME'])
#     print(os.environ['AWS_LAMBDA_LOG_STREAM_NAME'])
#     print('## EVENT')
#     print(event)




import os
import logging
logger = logging.getLogger()
logger.setLevel("INFO")
  
def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ['AWS_LAMBDA_LOG_GROUP_NAME'])
    logger.info(os.environ['AWS_LAMBDA_LOG_STREAM_NAME'])
    logger.info('## EVENT')
    logger.info(event)

# import logging  
# logger = logging.getLogger()

def lambda_handler(event, context):
    logger.info("Inside the handler function")

lambda_handler("event", "context")