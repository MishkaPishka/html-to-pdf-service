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


MAX_SUPPORTED_FILE_COUNT = os.environ.get('MAX_SUPPORTED_FILE_COUNT', 10)
OUTPUTS_FOLDER_NAME = "outputs"
TEMPLATES_FOLDER_NAME = "templates"

TEMPLATES_MAPPING = {
    TemplateNames.SIMPLE.value: os.path.join(Path(__file__).parent.absolute(), TEMPLATES_FOLDER_NAME,
                                             "template_simple.css"),
    TemplateNames.TODOLIST.value: os.path.join(Path(__file__).parent.absolute(), TEMPLATES_FOLDER_NAME,
                                               "template_todolist.css")}
