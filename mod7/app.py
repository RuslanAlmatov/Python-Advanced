import logging.config

import logging_tree as logging_tree

from utils import *
from logging_config import dict_config

logging.config.dictConfig(dict_config)

with open("logging_tree.txt", "w") as f:
    for line in logging_tree.format.build_description(node=None):
        f.write(line)

logger = logging.getLogger("app")
logger.info("Введите первое число: ")
number1 = input("Введите первое число: ")
logger.info("Введите операцию: ")
operation = input("Введите операцию: ")
logger.info("Введите второе число: ")
number2 = input("Введите второе число: ")
logger.debug("Введено выражение")
if (number1.isdigit()) or (number2.isdigit()):
    result = calculate(float(number1), operation, float(number2))
elif operation not in ["+", "*", "/", "-"]:
    logger.error("Вы ввели некорректную операцию")
    raise ValueError("Вы ввели некорректную операцию")
else:
    logger.error("Вы ввели не числа")
    raise ValueError("Вы ввели не числа")
logger.info(f"{number1} {operation} {number2} = {result}")
logger.info("ÎŒØ∏‡°⁄·°€йцукен")