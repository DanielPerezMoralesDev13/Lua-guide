#!/usr/bin/env python3

""" 
>>> Autor: Daniel Benjamin Perez Morales
>>> GitHub: https://github.com/DanielPerezMoralesDev13
>>> Correo electrónico: danielperezdev@proton.me
"""
import os
from sys import exit

def documentacionRepository() -> None:
    os.system(command="git add './README.md'")
    os.system(command="git commit -m 'README añadido'")
    os.system(command="git add './LICENSE'")
    os.system(command="git commit -m 'LICENSE añadido'")
    os.system(command="git add './.gitignore'")
    os.system(command="git commit -m '.gitignore añadido'")
    return None

def inicializarRepository() -> None:
    os.system(command="git init")
    os.system(command="git add ./script.py")
    return None

def filtrarLista(lista: list[str]) -> list[str]:
    lista_filtrada: list[str] = list()
    c: int = 0
    while c < 20:
        for i in lista:
            if c >= 18 and i not in lista_filtrada:
                lista_filtrada.append(i)
                # print(i)
                c += 1

            elif c < 18 and i[0:1:1].isdigit() and int(i[0:2:1]) ==  c and i not in lista_filtrada:
                lista_filtrada.append(i)
                # print(i)
                c += 1
    return lista_filtrada

def añadirFicherosDirectorios(lista_filtrada: list[str]) -> None:
    for _,i in enumerate(iterable=lista_filtrada,start=0):
        print(i)
        if _ >= 18:
            os.system(command=r"git add './Lua Language/{}'".format(i))
            os.system(command="git commit -m 'directorio {} añadido'".format(i))
        elif _ == 19:
            os.system(command=r"git add './Lua Language/{}'".format(i))
            os.system(command="git commit -m 'fichero {} añadido'".format(i))
        else:
            os.system(command=r"git add './Lua Language/{}'".format(i))
            os.system(command="git commit -m 'fichero {} añadido'".format(i))
    return lista_filtrada

def subirCambios(url_repository: str) -> None:
    os.system(command=f"git remote add origin {url_repository}")
    os.system(command="git push --set-upstream origin master")
 
def main() -> None:
    lista: list[str] = [str(i) for i in os.listdir(path=r"./Lua Language")]
    lista_filtrada: list[str] = filtrarLista(lista=lista)
    del lista
    inicializarRepository()
    añadirFicherosDirectorios(lista_filtrada=lista_filtrada)
    documentacionRepository()
    subirCambios(url_repository="https://github.com/DanielPerezMoralesDev13/Lua-guide.git")

    # print("\n".join(lista_filtrada))
    return None


if __name__ == "__main__":
    main()
    exit(0)
