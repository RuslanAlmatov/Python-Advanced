import logging

logger = logging.getLogger("utils")


def calculate(number1, operation, number2):
    if "+" == operation:
        logger.debug(f"{number1} + {number2}")
        return number1 + number2
    elif "*" == operation:
        logger.debug(f"{number1} * {number2}")
        return number1 * number2
    elif "-" == operation:
        logger.debug(f"{number1} - {number2}")
        return number1 - number2
    elif "/" == operation:
        if number2 == 0:
            logger.error("Can't divide by zero")
            raise ZeroDivisionError("На ноль делить нельзя")
        logger.debug(f"{number1} // {number2}")
        return number1 // number2
