class Task:
  """
  Represents a task with a description, date, and time.

  Attributes:
      description (str): Description of the task.
      date (str): Due date of the task (format: "MM/DD/YYYY").
      time (str): Due time of the task (format: "HH:MM").
  """

  def __init__(self, desc, date, time):
      """
      Initializes a Task object with the given description, date, and time.

      Args:
          desc (str): Description of the task.
          date (str): Due date of the task (format: "MM/DD/YYYY").
          time (str): Due time of the task (format: "HH:MM").
      """
      self.description = desc
      self.date = date
      self.time = time

  def __str__(self):
      """
      Returns a string representation of the task.

      Returns:
          str: String representation of the task.
      """
      return f"{self.description} - Due: {self.date} at {self.time}\n"

  def __repr__(self):
      """
      Returns a string representation of the task suitable for debugging.

      Returns:
          str: String representation of the task.
      """
      return f"{self.description},{self.date},{self.time}\n"

  def __lt__(self, other):
      """
      Compares two tasks based on their dates and times.

      Args:
          other (Task): Another Task object to compare with.

      Returns:
          bool: True if this task is earlier than the other task, False otherwise.
      """
      return self.date < other.date or (self.date == other.date and self.time < other.time)
