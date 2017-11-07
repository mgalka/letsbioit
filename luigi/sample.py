import luigi


class ReadChromosome(luigi.ExternalTask):
    input_file = luigi.Parameter(default="/tmp/input.txt")

    def run(self):
        print(self.input_file)
        # print("hello")
        source_file = open(self.input_file, 'r')

        f = self.output().open('w')
        f.close()

    def output(self):
        return luigi.LocalTarget(self.input_file + ".read")


class CountA(luigi.Task):
    input_file = luigi.Parameter(default="/tmp/input.txt")

    def requires(self):
        return ReadChromosome()

    def run(self):
        f = self.output().open('w')
        print >> f, "hello"
        f.close()

    def output(self):
        return luigi.LocalTarget(self.input_file + ".A")


class PrintAll(luigi.Task):
    input_file = luigi.Parameter(default="/tmp/input.txt")

    def requires(self):
        return [CountA(self.input_file)]


if __name__ == '__main__':
    luigi.run()
