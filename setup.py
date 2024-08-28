from cx_Freeze import setup, Executable
import os

# Define the main script file (entry point)
main_script = "home.py"

# Include additional files and directories
include_files = [
    os.path.join("ui"),  
    "final_federal_university.json",  
    "final_state_university.json",
]

# Setup information
setup(
    name="University Application",
    version="1.0",
    description="An application for managing universities",
    options={
        "build_exe": {
            "packages": ["os", "sys", "PyQt5"],  
            "includes": [],  
            "include_files": include_files,  
            "excludes": [],  
        }
    },
    executables=[
        Executable(
            main_script,
            base="Win32GUI",  
            target_name="UniversityApp.exe",  
            icon="path/to/icon.ico"  
        )
    ]
)
