# Levels: Debug, Info, Warning, Error, Critical

import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

print(dir(logging))

# create and config logger
logging.basicConfig(filename = 'Luberjack.log', level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')
logger = logging.getLogger()

# logger.info("Our first message...")
logger.info("Our second message...")
print(logger.level)


# Test messages
logger.debug("This is a harmless debug message..")
logger.info("Just some useful info..")
logger.warning("I'm sorry , but I can't do that, Dave..")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")




