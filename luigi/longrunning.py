import re
from time import sleep

import luigi
from os import listdir

from os.path import dirname, basename

import luigi


class LongRunningParent(luigi.Task):
    def requires(self):
        return [
            LongRunning('a'),
            LongRunning('b'),
            LongRunning('c'),
            LongRunning('d'),
            LongRunning('e'),
            LongRunning('f'),
            LongRunning('g'),
        ]

    def run(self):
        self.output().open('w').close()

    def output(self):
        return luigi.LocalTarget("long-running-parent")


class LongRunning(luigi.Task):
    name = luigi.Parameter()

    def requires(self):
        return [QuickRunning('a')]

    def run(self):
        sleep(10)
        self.output().open('w').close()

    def output(self):
        return luigi.LocalTarget("long-running" + self.name)


class QuickRunning(luigi.Task):
    name = luigi.Parameter()

    def run(self):
        sleep(1)
        self.output().open('w').close()

    def output(self):
        return luigi.LocalTarget("long-running-quick" + self.name)


if __name__ == '__main__':
    luigi.run()
