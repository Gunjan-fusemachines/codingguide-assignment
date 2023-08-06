from abc import ABC, abstractmethod

# Product: Logger interface
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# Concrete Product: FileLogger
class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as file:
            file.write(f'File Log: {message}\n')

# Concrete Product: ConsoleLogger
class ConsoleLogger(Logger):
    def log(self, message):
        print(f'Console Log: {message}')

# Concrete Product: DatabaseLogger
class DatabaseLogger(Logger):
    def __init__(self, database_connection):
        self.db_connection = database_connection

    def log(self, message):
        self.db_connection.execute(f'INSERT INTO logs (message) VALUES ("{message}")')

# Factory: LoggerFactory
class LoggerFactory:
    @staticmethod
    def create_logger(logger_type, *args, **kwargs):
        print(f"Creating logger of type: {logger_type}")
        if logger_type == 'file':
            return FileLogger(*args)
        elif logger_type == 'console':
            return ConsoleLogger()
        elif logger_type == 'database':
            return DatabaseLogger(*args)

# Client code
def main():
    logger_type = 'file'
    logger = LoggerFactory.create_logger(logger_type, 'design-patterns/logs.txt')

    logger.log('This is a log message.')
    logger.log('Another log message.')

if __name__ == "__main__":
    main()
