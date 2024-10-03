from task import Task

class Tasklist:
    """
    Represents a list of tasks.

    Attributes:
        tasklist (list): A list containing Task objects representing tasks.
    """

    def __init__(self):
        """
        Initializes a Tasklist object by reading tasks from a file and sorting them.
        """
        self.tasklist = []
        with open('tasklist.txt', 'r') as file:
            for line in file:
                # Check if the line contains at least three values
                if ',' not in line:
                    continue  # Skip this line if it doesn't contain the expected format
                desc, date, time = line.strip().split(',', 2)  # Split at most 2 times
                self.tasklist.append(Task(desc, date, time))
            self.tasklist.sort()

    def add_task(self, desc, date, time):
        """
        Adds a new task to the tasklist.

        Args:
            desc (str): Description of the task.
            date (str): Due date of the task (format: "MM/DD/YYYY").
            time (str): Due time of the task (format: "HH:MM").
        """
        self.tasklist.append(Task(desc, date, time))
        self.tasklist.sort()

    def get_current_task(self):
        """
        Retrieves the current task from the tasklist.

        Returns:
            Task: The current task.
        """
        return self.tasklist[0]

    def mark_complete(self):
        """
        Marks the current task as complete by removing it from the tasklist.

        Returns:
            Task: The completed task.
        """
        task = self.tasklist[0]
        print(task)
        return self.tasklist.pop(0)

    def save_file(self):
        """
        Saves the tasklist to a file.
        """
        with open('tasklist.txt', 'w') as file:
            for task in self.tasklist:
                file.write(repr(task) + '\n')

    def __len__(self):
        """
        Returns the number of tasks in the tasklist.

        Returns:
            int: Number of tasks.
        """
        return len(self.tasklist)

    def __iter__(self):
        """
        Initializes iteration over the tasklist.

        Returns:
            Tasklist: The Tasklist object.
        """
        self.n = 0
        return self

    def __next__(self):
        """
        Retrieves the next task during iteration.

        Returns:
            Task: The next task.

        Raises:
            StopIteration: If there are no more tasks to iterate over.
        """
        if self.n < len(self.tasklist):
            result = self.tasklist[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration
