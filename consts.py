import os
from enum import Enum
from pathlib import Path


class SourceTypes(Enum):
    STRING = "string"
    URL = "url"
    FILE = "file"


class TemplateNames(Enum):
    SIMPLE = "simple"
    TODOLIST = "todolist"
    SKILL_BAR = "skill_bar"


MAX_SUPPORTED_FILE_COUNT = os.environ.get('MAX_SUPPORTED_FILE_COUNT', 10)
OUTPUTS_FOLDER_NAME = "outputs"
TEMPLATES_FOLDER_NAME = "templates"

TEMPLATES_FOLDER_PATH = os.path.join(Path(__file__).parent.absolute(), TEMPLATES_FOLDER_NAME)
