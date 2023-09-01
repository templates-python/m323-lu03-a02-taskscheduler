import time
import main
def test_task_execution_order():
    executed_tasks = []

    def task1():
        executed_tasks.append('Task 1 executed!')

    def task2():
        executed_tasks.append('Task 2 executed!')

    tasks = [task1, task2]
    delay = 1

    main.task_scheduler(tasks, delay)

    assert executed_tasks == ['Task 1 executed!', 'Task 2 executed!'], f'Expected ["Task 1 executed!", "Task 2 executed!"], got {executed_tasks}'

def test_task_execution_with_delay():
    def task1():
        pass

    def task2():
        pass

    tasks = [task1, task2]
    delay = 1  # 1 second delay

    start_time = time.time()
    main.task_scheduler(tasks, delay)
    end_time = time.time()

    elapsed_time = end_time - start_time

    # Überprüfen, ob die tatsächlich verstrichene Zeit ungefähr der erwarteten Zeit entspricht.
    assert abs(elapsed_time - 2.0) < 0.1, f'Expected around 2.0 seconds, got {elapsed_time} seconds'

def test_task_execution_order_expert():
    executed_tasks = []

    def task1():
        executed_tasks.append('Task 1 executed!')

    def task2():
        executed_tasks.append('Task 2 executed!')

    tasks = [task1, task2]
    delays = [1, 2]

    main.task_scheduler_expert(tasks, delays)

    assert executed_tasks == ['Task 1 executed!', 'Task 2 executed!'], f'Expected ["Task 1 executed!", "Task 2 executed!"], got {executed_tasks}'

def test_task_execution_with_individual_delays():
    executed_tasks = []

    def task1():
        executed_tasks.append((2, time.time()))

    def task2():
        executed_tasks.append((3, time.time()))

    tasks = [task1, task2]
    delays = [2, 3]

    start_time = time.time()
    main.task_scheduler_expert(tasks, delays)
    end_time = time.time()


    elapsed_time_task1 = executed_tasks[1][1] - start_time
    elapsed_time_task2 = end_time - executed_tasks[1][1]

    # Überprüfen, ob die tatsächlich verstrichene Zeit ungefähr der erwarteten Zeit entspricht.
    assert abs(elapsed_time_task1 - 2) < 0.1, f'Expected around 1 second for task 1, got {elapsed_time_task1} seconds'
    assert abs(elapsed_time_task2 - 3) < 0.1, f'Expected around 3 seconds for task 2, got {elapsed_time_task2} seconds'


