import sys


def txt_importer(path_file):
    if '.txt' not in path_file:
        return sys.stderr.write("Formato inválido\n")
    try:
        file = open(path_file, mode="r")
        return file.read().split("\n")
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
