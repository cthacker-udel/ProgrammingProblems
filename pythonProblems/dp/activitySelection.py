from __future__ import annotations
from typing import List

class Task:
    """
    The Task class, represents an task with an required time
    """

    def __init__(self, id: int, required: int):
        """
        Constructs a new activity instance

        Args:
            id (int): The id of the task
            required (int): Time required to complete
        """
        self.id = id
        self.required = required

    def to_string(self):
        return f'[Id {self.id} | Required {self.required}]'

    def to_string_total(self, total):
        print(f'{self.to_string()} total {total}')

def calculate_total_cost(tasks: List[Task]) -> float: ## couldn't we just sort the array of tasks?
    ## sort tasks by
    sorted_tasks = sorted(tasks, key=lambda x: x.required)
    running_total = 0
    for eachtask in sorted_tasks:
        running_total = running_total + (eachtask.required + running_total)
    print(running_total)
    return running_total / len(tasks)
        ## choose task, find most compatible, choosing the task involves finding it's least counterpart,
        ## aka if a + (b + a) < b + (a + b), or if a = 3 and b = 5, we want 3 + 8 vs 5 + 8



if __name__ == "__main__":
    activity_values = [5, 3, 2, 1, 10]
    activity_array = [Task(taskId, taskCost) for taskId, taskCost in enumerate(activity_values)]
    print(calculate_total_cost(activity_array))
