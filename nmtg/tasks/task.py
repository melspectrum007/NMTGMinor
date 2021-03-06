import logging
from argparse import ArgumentParser

logger = logging.getLogger(__name__)


class Task:
    @staticmethod
    def add_options(parser: ArgumentParser):
        """Add task-specific command line options"""
        raise NotImplementedError

    @classmethod
    def setup_task(cls, args):
        """Setup the task (e.g. load dictionaries, datasets etc.)"""
        raise NotImplementedError

    def score_results(self, results):
        """Calculate task-specific score(s) on the validation dataset.
        :return List of strings describing the results"""
        raise NotImplementedError

    def save_results(self, results, out_filename):
        """Save the results (probably generated by a solution) in a task-specific format."""
        raise NotImplementedError

    def load_results(self, filename):
        """Load some results from disk, for scoring"""
        raise NotImplementedError
