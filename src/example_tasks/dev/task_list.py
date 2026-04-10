from fractal_task_tools.task_models import ParallelTask

TASK_LIST = [
    ParallelTask(name="task1_scalars", executable="task1_scalars.py"),
    ParallelTask(name="task2_arrays", executable="task2_arrays.py"),
    ParallelTask(name="task3_objects", executable="task3_objects.py"),
    ParallelTask(name="task4_pydantic_models", executable="task4_pydantic_models.py"),
    ParallelTask(
        name="task6_conditional_expressions",
        executable="task6_conditional_expressions.py",
    ),
]
