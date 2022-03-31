"""Olympics log filters."""
import logging


class DebugFilter(logging.Filter):
    """Filter messages with DEBUG level."""
    def filter(self, record):
        return record.levelno in [logging.DEBUG]


class InfoFilter(logging.Filter):
    """Filter messages with INFO and WARNING level."""
    def filter(self, record):
        return record.levelno in [logging.INFO, logging.WARNING]


class ErrorFilter(logging.Filter):
    """Filter messages with ERROR and CRITICAL level."""
    def filter(self, record):
        return record.levelno in [logging.ERROR, logging.CRITICAL]
