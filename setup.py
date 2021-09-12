import cx_Freeze

executables = [cx_Freeze.Executable("script.py")]

cx_Freeze.setup(
    name="snakeathon",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":[".idea/checker.png"]}},
    executables = executables
    )