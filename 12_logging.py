# %% -- IMPORT LIBRARIES
import logging

# %% -- SOME TYPES OF LOGS
# -- Less critical
logging.debug("debug")
logging.info("info")

# -- More critical
logging.error("error")
logging.warning("warning")
logging.critical("critical")

# %% -- USING BASICCONFIG() TO GENERATE LOG FILE
# -- format = "%(asctime)s: %(levelname)s: %(message)s " --> showing Date/Time - Level of log - message
logging.basicConfig(filename="D:\\00_MASTER OF COMPUTER SCIENCE_MUM\\00_Projects\\12_Automation Testing_Basic\\logs\\log1.log",
                    format="%(asctime)s: %(levelname)s: %(message)s ",
                    level=logging.DEBUG
)

logging.debug("debug")
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")

# %% -- CREATE A LOGGER OBJECT INSTEAD OF USING THE LOGGING DIRECTLY
logging.basicConfig(filename="D:\\00_MASTER OF COMPUTER SCIENCE_MUM\\00_Projects\\12_Automation Testing_Basic\\logs\\log1.log",
                    format="%(asctime)s: %(levelname)s: %(message)s ",
                    level=logging.DEBUG
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("debug")
logger.info("info")
logger.error("error")
logger.warning("warning")
logger.critical("critical")


