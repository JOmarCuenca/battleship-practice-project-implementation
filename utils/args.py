import argparse
from dataclasses import dataclass

from constants.log_level import LogLevel

@dataclass(frozen=True, repr=True, eq=True)
class Args:
    verbose: bool
    log_level: str
    log_file_extension: str

    def __str__(self) -> str:
        return str(
            {
                'verbose': self.verbose,
                'log_level': self.log_level,
                'log_file_extension': self.log_file_extension,
            },
        )

    def parseArgs():
        parser = argparse.ArgumentParser(
            prog='Battleship Game Project',
            description='Battleship Game Project Practice',
        )

        parser.add_argument(
            '-v',
            '--verbose',
            action='store_true',
            dest='verbose',
            help='Increase output verbosity',
        )

        parser.add_argument(
            '--log-level',
            dest='log_level',
            default=LogLevel.INFO.name,
            help='Set log level to debug, info, warning, error, critical',
            choices=[level.name for level in LogLevel],
            type=str.upper,
            metavar='LOG_LEVEL',
        )

        parser.add_argument(
            '--log_file_extension',
            dest='log_file_extension',
            default='run',
            help='Set log file extension path',
            type=str,
            metavar='LOG_FILE_EXTENSION_PATH',
        )

        args = parser.parse_args()

        return Args(**args.__dict__)
