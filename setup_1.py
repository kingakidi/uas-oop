from cx_Freeze import setup, Executable
import os

# Include the entire "fields data" directory
include_files = [
    "ui",                        
    "final_federal_university.json",
    "final_state_university.json",
    ("fields data", "fields data"),   
]

# Define the target executable
# executables = [
#     Executable("home.py", target_name="your_application_name.exe")
# ]

executables=[
        Executable(
           "home.py",
            base="Win32GUI",  
            target_name="UniversityApp.exe",  
            icon="path/to/icon.ico"  
        )
    ]

# Setup configuration
setup(
    name="UniversityApp.exe",
    version="1.0",
    description="A University Admission System",
    options={
        "build_exe": {
            "packages": ["os", "sys", "json"],  
            "include_files": include_files,     
            "excludes": [],            
        }
    },
    executables=executables
)
