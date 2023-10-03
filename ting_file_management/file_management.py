import sys


def txt_importer(path_file):
    if '.txt' not in path_file:
        return sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, mode="r") as file:
            return file.read().split("\n")
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
