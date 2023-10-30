import os

def add_line_to_files(path, extension, line_to_add):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()

                with open(file_path, 'a') as f:
                    f.write(f"\n{line_to_add}")

                print(f"Added line to {file}")

path = 'src/content/docs/en/pages/main-menu/reference/build/edge-application/domains'
extension = '.mdx'
line_to_add = """
---

**Contributors** <ContributorList>Contributor</ContributorList>
"""

add_line_to_files(path, extension, line_to_add)
