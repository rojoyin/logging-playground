import logging

from logging_playground.the_project import base, utils
# import logging_playground.the_project as project


# print(project.logger)
# print(base.logger)
# print(utils.logger)
# print(base.logger.handlers)
# print(base.logger.parent.handlers)
# print(base.logger.parent)


logger = logging.getLogger(__name__)
logger.debug("debug called from main")

base.func1()
utils.func2()
