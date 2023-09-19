# BASSA KOFFI FRANCK DONALD - MASTER 2IA
import os
import subprocess

class ProjectInitializer:
    def create_project_structure(self):
        self.create_folders()
        self.create_files()

    def create_folders(self):
        folders = ['data', 'data/cleaned', 'data/processed', 'data/raw',
                   'docs', 'models', 'notebooks', 'reports', 'src']
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
            subprocess.call(['git', 'add', folder])
            subprocess.call(['git', 'commit', '-m', f'Création du dossier {folder}'])

    def create_files(self):
        files = ['.gitignore', 'LICENSE.md', 'notebooks/main.ipynb', 'README.md',
                 'reports/requirements.txt', 'src/utils.py', 'src/process.py', 'src/train.py']
        for file in files:
            if '.' in file:
                open(file, 'w').close()
                subprocess.call(['git', 'add', file])
                subprocess.call(['git', 'commit', '-m', f'Création du fichier {file}'])
            else:
                os.makedirs(file, exist_ok=True)

    def update_readme(self, text):
        with open('README.md', 'a') as readme_file:
            readme_file.write(text)
        subprocess.call(['git', 'add', 'README.md'])
        subprocess.call(['git', 'commit', '-m', 'Ajout du texte du README'])

if __name__ == "__main__":
    initializer = ProjectInitializer()
    initializer.create_project_structure()
    initializer.update_readme('ce programme permet de créer une aborescence de fichier et dossier. il crée plusieurs commit et les dépose sur une branche.')
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', 'Ajout de tous les fichiers'])
    subprocess.call(['git', 'push'])