import re

import luigi
from os import listdir

from os.path import dirname, basename

import luigi

class ReadChromosome(luigi.Task):
    input_file = luigi.Parameter()

    def requires(self):
        return [CountLetter(self.input_file, 'A'),
                CountLetter(self.input_file, 'T'),
                CountLetter(self.input_file, 'G'),
                CountLetter(self.input_file, 'C')]

    def run(self):
        print(self.input_file)
        with self.output().open('w') as out:
            out.write('stats')

    def output(self):
        return luigi.LocalTarget(self.input_file + '.read')


class CountLetter(luigi.Task):
    # bacteriophag 4a
    input_file = luigi.Parameter()
    letter = luigi.Parameter()

    def run(self):
        print(self.input_file)
        found = 0

        with open(str(self.input_file), 'r') as input:
            # skip header
            input.readline()

            line = input.readline()
            while line:
                line = input.readline()
                found = found + line.count(str(self.letter))

        with self.output().open('w') as out:
            out.write(str(found))

    def output(self):
        return luigi.LocalTarget(str(self.input_file) + '.' + str(self.letter))


class PrintAll(luigi.Task):
    input_file = luigi.Parameter(default='/Users/astasiak/Documents/bioit/letsbioit/luigi/sequence.fasta')

    def requires(self):
        return ReadChromosome(self.input_file)

    def run(self):
        base_name = basename(self.input_file)
        pattern = re.compile('^' + base_name + '\..$')
        dir_name = dirname(self.input_file)

        files = [x for x in listdir(dir_name) if pattern.match(basename(x))]

        with self.output().open('w') as out:
            for file in files:
                with open(file, 'r') as f:
                    out.write(file.split('.')[-1])
                    out.write(' ')
                    out.write(f.readline())
                    out.write('\n')

    def output(self):
        return luigi.LocalTarget(self.input_file + '.summary')


if __name__ == '__main__':
    luigi.run()
