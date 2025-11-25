#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI Principal do Compilador MiniLang.
Aceita um arquivo .min como argumento e executa o pipeline completo:
1. Lexing (ANTLR)
2. Parsing (ANTLR)
3. AST Building
4. Semantic Analysis
5. Interpretation + Code Generation
"""

import sys
import os
import argparse
from pathlib import Path

# Imports locais
from src.ast_nodes import Program, Block
from src.pretty import print_ast_ascii
from src.sema import check_semantics, print_symtab, SemanticError
from src.interp import exec_program, RuntimeErrorLang
from src.codegen import codegen_python, exec_generated_python


def generate_antlr_code():
    """Gera código ANTLR usando a ferramenta antlr4."""
    grammar_dir = Path("grammar")
    generated_dir = Path("src/generated")

    if not grammar_dir.exists():
        print(f"Erro: diretório {grammar_dir} não encontrado.")
        return False

    try:
        import subprocess
        # Tenta usar antlr4 se disponível (instalado via pip)
        result = subprocess.run([
            "antlr4", "-Dlanguage=Python3", "-visitor",
            "-o", str(generated_dir),
            str(grammar_dir / "MiniLang.g4")
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Erro ao gerar código ANTLR: {result.stderr}")
            return False

        print("Código ANTLR gerado com sucesso em src/generated/")
        return True
    except FileNotFoundError:
        print("Aviso: antlr4 não encontrado no PATH. Tente instalar com:")
        print("  pip install antlr4-python3-runtime")
        print("  # e fazer download do antlr-4.13.2-complete.jar")
        return False


def compile_and_run(input_file: str, trace: bool = False, codegen_mode: bool = False):
    """
    Compila e executa um arquivo MiniLang.
    """
    input_path = Path(input_file)

    if not input_path.exists():
        print(f"Erro: arquivo '{input_file}' não encontrado.")
        return False

    print(f"=== Compilando {input_file} ===\n")

    try:
        # Lê o código-fonte
        with open(input_path, 'r', encoding='utf-8') as f:
            source_code = f.read()

        # ===== FASE 1: Lexing + Parsing (ANTLR) =====
        print("[1/5] Análise Léxica e Sintática...")
        try:
            from antlr4 import InputStream, CommonTokenStream
            from src.generated.MiniLangLexer import MiniLangLexer
            from src.generated.MiniLangParser import MiniLangParser
            from src.ast_builder import ASTBuilder
        except ImportError:
            print("Erro: código ANTLR não gerado. Execute: python cli.py --generate-antlr")
            return False

        input_stream = InputStream(source_code)
        lexer = MiniLangLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MiniLangParser(stream)

        # Parse
        parse_tree = parser.program()

        # ===== FASE 2: AST Building =====
        print("[2/5] Construção da AST...")
        builder = ASTBuilder()
        ast = builder.visit(parse_tree)

        if ast is None:
            print("Erro: falha ao construir AST.")
            return False

        # ===== FASE 3: Análise Semântica =====
        print("[3/5] Análise Semântica...")
        try:
            symtab = check_semantics(ast)
        except SemanticError as e:
            print(f"Erro Semântico: {e}")
            return False

        # Imprime AST
        print("\n=== ÁRVORE SINTÁTICA ABSTRATA (AST) ===")
        print_ast_ascii(ast)

        # Imprime Tabela de Símbolos
        print()
        print_symtab(symtab)

        # ===== FASE 4: Interpretação =====
        print("\n[4/5] Execução (Intérprete)...")
        print("--- Saída do Intérprete ---")
        try:
            env_interp = exec_program(ast, trace=trace)
        except RuntimeErrorLang as e:
            print(f"Erro em Tempo de Execução: {e}")
            return False

        # ===== FASE 5: Geração de Código e Execução =====
        print("\n[5/5] Geração de Código Python...")
        py_code = codegen_python(ast)

        if codegen_mode:
            print("\n--- Código Python Gerado ---")
            print(py_code)

        print("\n--- Saída do Código Gerado ---")
        try:
            env_codegen = exec_generated_python(py_code)
        except Exception as e:
            print(f"Erro ao Executar Código Gerado: {e}")
            return False

        print("\n=== COMPILAÇÃO BEM-SUCEDIDA ===")
        return True

    except Exception as e:
        print(f"Erro Inesperado: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    parser = argparse.ArgumentParser(description="Compilador MiniLang")
    parser.add_argument(
        "input_file",
        nargs='?',
        help="Arquivo .min a compilar"
    )
    parser.add_argument(
        "--generate-antlr",
        action="store_true",
        help="Gera código ANTLR a partir de grammar/MiniLang.g4"
    )
    parser.add_argument(
        "--trace",
        action="store_true",
        help="Executa com trace (debug)"
    )
    parser.add_argument(
        "--codegen",
        action="store_true",
        help="Imprime código Python gerado"
    )

    args = parser.parse_args()

    if args.generate_antlr:
        generate_antlr_code()
        return

    if not args.input_file:
        parser.print_help()
        return

    compile_and_run(args.input_file, trace=args.trace, codegen_mode=args.codegen)


if __name__ == "__main__":
    main()
