class Livro:
    def __init__(self, titulo, autor, livro_id):
        self.titulo = titulo
        self.autor = autor
        self.livro_id = livro_id
        self.status = "Disponível"

    def emprestar(self):
        if self.status == "Disponível":
            self.status = "Emprestado"
            return True
        return False

    def devolver(self):
        if self.status == "Emprestado":
            self.status = "Disponível"
            return True
        return False

class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico = []

    def adicionar_emprestimo(self, livro):
        self.historico.append(livro)

    def remover_emprestimo(self, livro):
        if livro in self.historico:
            self.historico.remove(livro)

class Biblioteca:
    def __init__(self):
        self.catalogo = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.catalogo[livro.livro_id] = livro

    def adicionar_membro(self, membro):
        self.membros[membro.numero_membro] = membro

    def emprestar_livro(self, livro_id, numero_membro):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(numero_membro)
        if livro and membro and livro.emprestar():
            membro.adicionar_emprestimo(livro)
            return f"Livro '{livro.titulo}' emprestado para {membro.nome}."
        return "Não foi possível realizar o empréstimo."

    def devolver_livro(self, livro_id, numero_membro):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(numero_membro)
        if livro and membro and livro.devolver():
            membro.remover_emprestimo(livro)
            return f"Livro '{livro.titulo}' devolvido por {membro.nome}."
        return "Não foi possível realizar a devolução."

    def pesquisar_livro(self, **kwargs):
        resultados = []
        for livro in self.catalogo.values():
            if all(getattr(livro, k, None) == v for k, v in kwargs.items()):
                resultados.append(livro)
        return resultados
    

import tkinter as tk
from tkinter import messagebox

class BibliotecaApp:
    def __init__(self, root):
        self.biblioteca = Biblioteca()
        self.root = root
        self.root.title("Biblioteca")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Labels e Entradas para livros
        self.livro_id_label = tk.Label(self.frame, text="ID do Livro")
        self.livro_id_label.grid(row=0, column=0)
        self.livro_id_entry = tk.Entry(self.frame)
        self.livro_id_entry.grid(row=0, column=1)

        self.livro_titulo_label = tk.Label(self.frame, text="Título")
        self.livro_titulo_label.grid(row=1, column=0)
        self.livro_titulo_entry = tk.Entry(self.frame)
        self.livro_titulo_entry.grid(row=1, column=1)

        self.livro_autor_label = tk.Label(self.frame, text="Autor")
        self.livro_autor_label.grid(row=2, column=0)
        self.livro_autor_entry = tk.Entry(self.frame)
        self.livro_autor_entry.grid(row=2, column=1)

        # Labels e Entradas para membros
        self.membro_nome_label = tk.Label(self.frame, text="Nome do Membro")
        self.membro_nome_label.grid(row=3, column=0)
        self.membro_nome_entry = tk.Entry(self.frame)
        self.membro_nome_entry.grid(row=3, column=1)

        self.membro_numero_label = tk.Label(self.frame, text="Número do Membro")
        self.membro_numero_label.grid(row=4, column=0)
        self.membro_numero_entry = tk.Entry(self.frame)
        self.membro_numero_entry.grid(row=4, column=1)

        # Botões para operações
        self.add_livro_button = tk.Button(self.frame, text="Adicionar Livro", command=self.adicionar_livro)
        self.add_livro_button.grid(row=5, column=0, pady=5)

        self.add_membro_button = tk.Button(self.frame, text="Adicionar Membro", command=self.adicionar_membro)
        self.add_membro_button.grid(row=5, column=1, pady=5)

        self.emprestar_button = tk.Button(self.frame, text="Emprestar Livro", command=self.emprestar_livro)
        self.emprestar_button.grid(row=6, column=0, pady=5)

        self.devolver_button = tk.Button(self.frame, text="Devolver Livro", command=self.devolver_livro)
        self.devolver_button.grid(row=6, column=1, pady=5)

    def adicionar_livro(self):
        livro_id = self.livro_id_entry.get()
        titulo = self.livro_titulo_entry.get()
        autor = self.livro_autor_entry.get()
        if livro_id and titulo and autor:
            livro = Livro(titulo, autor, livro_id)
            self.biblioteca.adicionar_livro(livro)
            messagebox.showinfo("Info", f"Livro '{titulo}' adicionado.")
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    def adicionar_membro(self):
        nome = self.membro_nome_entry.get()
        numero_membro = self.membro_numero_entry.get()
        if nome and numero_membro:
            membro = Membro(nome, numero_membro)
            self.biblioteca.adicionar_membro(membro)
            messagebox.showinfo("Info", f"Membro '{nome}' adicionado.")
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    def emprestar_livro(self):
        livro_id = self.livro_id_entry.get()
        numero_membro = self.membro_numero_entry.get()
        result = self.biblioteca.emprestar_livro(livro_id, numero_membro)
        messagebox.showinfo("Info", result)

    def devolver_livro(self):
        livro_id = self.livro_id_entry.get()
        numero_membro = self.membro_numero_entry.get()
        result = self.biblioteca.devolver_livro(livro_id, numero_membro)
        messagebox.showinfo("Info", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()