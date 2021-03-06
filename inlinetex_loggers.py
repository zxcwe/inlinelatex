"""
This hosts configuration code for InlineLaTeX's three loggers:
- server_logger logs the telepot server's activity
- tex_logger follows the call stack of the process() function in latex_generator.py
- tex_cmd_output_logger is not yet implemented
"""

import logging
from sys import stdout


def initialize_loggers():
    # logger for inlinetexbot.py
    server_formatter = logging.Formatter("%(asctime)s: %(message)s")

    server_handler = logging.StreamHandler(stream=stdout)
    server_handler.setFormatter(server_formatter)

    server_logger = logging.getLogger('server_logger')
    server_logger.setLevel(logging.INFO)
    server_logger.addHandler(server_handler)

    # logger for the logic in latex_generator.py
    tex_formatter = logging.Formatter("\t%(message)s")

    tex_handler = logging.StreamHandler(stream=stdout)
    tex_handler.terminator = ''
    tex_handler.setFormatter(tex_formatter)

    tex_logger = logging.getLogger('tex_logger')
    tex_logger.setLevel(logging.INFO)
    tex_logger.addHandler(tex_handler)

    # logger for the output of the pdflatex command
    # TODO use this in latex_generator.py
    tex_cmd_output_logger = logging.getLogger('tex_cmd_output_logger')
    tex_cmd_output_logger.setLevel(logging.INFO)
