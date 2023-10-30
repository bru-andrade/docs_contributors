import os

def add_line_to_files(path, extension, line_to_add):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    f.close()

                with open(file_path, 'a') as f:
                    f.write(f"\n{line_to_add}")
                    f.close()

                print(f"Added line to {file}")

path = '/Users/bruna.andrade/VSCode/docs/src/content/docs/pt-br/pages/peering'
extension = '.mdx'
line_to_add = """

---

import ContributorList from '~/components/ContributorList.astro'

**Contribuidores** <ContributorList>Contributor</ContributorList>
"""

add_line_to_files(path, extension, line_to_add)
