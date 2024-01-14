import argparse
from dataclasses import dataclass

from constants.ai_player_difficulty import AIPlayerDifficulty
from constants.log_level import LogLevel


@dataclass(frozen=True, repr=True, eq=True)
class Args:
    verbose: bool
    log_level: LogLevel
    log_file_extension: str
    horizontal: bool
    pvp: bool
    pvc: AIPlayerDifficulty

    def __str__(self) -> str:
        return str(
            {
                'verbose': self.verbose,
                'log_level': self.log_level,
                'log_file_extension': self.log_file_extension,
                'horizontal': self.horizontal,
                'pvp': self.pvp,
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
            default=LogLevel.INFO,
            help='Set log level to debug, info, warning, error, critical',
            choices=list(LogLevel),
            type=LogLevel,
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

        parser.add_argument(
            '--horizontal',
            action='store_true',
            dest='horizontal',
            help='Set gameplay direction to horizontal',
        )

        parser.add_argument(
            '--pvc',
            dest='pvc',
            default=AIPlayerDifficulty.EASY,
            help='Set gameplay difficulty to player vs computer. Options: EASY, MEDIUM',
            type=AIPlayerDifficulty,
            choices=list(AIPlayerDifficulty),
            metavar='PVC',
        )

        parser.add_argument(
            '--pvp',
            action='store_true',
            dest='pvp',
            help='Set gameplay to player vs player',
        )

        args = parser.parse_args()

        return Args(**args.__dict__)
