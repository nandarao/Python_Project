import logging
   
#  
# logging.basicConfig(filename="C://Users//kishorenm//eclipse-workspace//nopcommercePythonProj//logs//logger.log",
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
#                      
# logger=logging.getLogger()
# logger.setLevel(logging.INFO)
# logger.info("test")
# logger.error("error")
 



class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\kishorenm\\eclipse-workspace\\nopcommercePythonProj\\logs\\logger.log",
                            format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

# test12=LogConfig.loggen()
# test12.info("msg")

