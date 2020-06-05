# -*- coding: utf-8 -*-
import logging
  
def log_file(file_path):  
    def log(func):

        def wrap_log(*args, **kwargs):
            name = func.__name__
            logger = logging.getLogger(name)
            logger.setLevel(logging.INFO)
            log_file = logging.FileHandler(file_path)
            log_format = '%(asctime)s - %(levelname)s - %(message)s'
            formatter = logging.Formatter(log_format)
            log_file.setFormatter(formatter)
            logger.addHandler(log_file)
            logger.info(f"Вызов функции: {name} c аргументами {' ,'.join(str(x) for x in args)}")
            result = func(*args, **kwargs)
            logger.info("Результат: %s" % result)
            return func

        return wrap_log
    return log

@log_file('funtions.log') 
def double_function(a):
    return a * 2
  
  
if __name__ == "__main__":
    value = double_function(2)