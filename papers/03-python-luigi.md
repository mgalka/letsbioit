% Python

# Luigi
## What is Luigi
Luigi is framework used for managing long running jobs and making sure the processing is fully executed.

## Installation

```bash
pip install luigi==2.7.1
```

## Running Luigi locally

```bash
luigi --module top_artists AggregateArtists --local-scheduler --date-interval 2012-06
```

## Basic building blocks
- `Target` - usually a single file `LocalTarget` or a database entry `MySqlTarget` it is the source and/or the destination of the processing done by the `Task`
- `Task` - single step in processing workflow, it might be reading the content of the file, running a command or just a milestone when all of the previous tasks were executed
- `Parameter` -
- `Dependency`

## Task
![](images/png/task_breakdown.png)

## Task
This is where computation is done. It consists of:
- `param = luigi.Parameter(default=42)` - parameter declaration
- `requires()` - defines a list of tasks that need to be finished before current task is executed
- `run()` - this is where computation happens
- `output()` - returns a `Target` where the output is saved

## Parameters

```python
import luigi
class DailyReport(luigi.Task)
    date = luigi.DateParameter(default=datetime.date.today())
```

You can pass a date via command line

```bash
--date 2012-05-10
```

## Function definition in Python

```python
def new_book(title, author, cover_type='paperback',
             available=True):
    # ... do stuff
    return result
```

- Functions in Python are defined with the keyword `def`.
- There are 2 types of parameters:
  - positional
  - keyword
