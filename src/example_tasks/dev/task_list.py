from fractal_task_tools.task_models import NonParallelTask

TASK_LIST = [
    NonParallelTask(name="task1_scalars", executable="task1_scalars.py"),
    NonParallelTask(name="task2_arrays", executable="task2_arrays.py"),
    NonParallelTask(name="task3_objects", executable="task3_objects.py"),
    # NonParallelTask(name="task4", executable="task4.py"),
    # NonParallelTask(name="task5", executable="task5.py"),
    NonParallelTask(
        name="task6_conditional_expressions",
        executable="task6_conditional_expressions.py",
    ),
]
