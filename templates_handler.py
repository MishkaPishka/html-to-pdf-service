import os

from consts import TEMPLATES_FOLDER_PATH


def save_template(template_data: str, template_name: str):
    filename = template_name + ".css"
    try:
        data_as_bytes = bytes(template_data, "utf-8")
        full_file_path = os.path.join(TEMPLATES_FOLDER_PATH, filename)
        with open(full_file_path, "wb") as binary_file:
            binary_file.write(data_as_bytes)
            return template_name
    except Exception as e:
        print(e.__cause__)
        return "Error In Uploading Template"


def get_template_names():
    # read templates folder and return file names without css
    obj = os.scandir(TEMPLATES_FOLDER_PATH)
    print("Files and Directories in '% s':" % TEMPLATES_FOLDER_PATH)
    template_names = []
    for entry in obj:
        if entry.is_dir() or entry.is_file():
            template_names.append(entry.name.replace('.css', ''))
    return template_names



if __name__ == "__main__":
    get_template_names()
