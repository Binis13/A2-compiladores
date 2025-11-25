#!/usr/bin/env python3
"""
Script para gerar código ANTLR4 usando Java diretamente.
"""

import subprocess
import os
import sys
from pathlib import Path

def download_antlr_jar():
    """Baixa o JAR do ANTLR4 se não existir."""
    antlr_dir = Path(__file__).parent / "tools"
    antlr_dir.mkdir(exist_ok=True)
    jar_path = antlr_dir / "antlr-4.13.0-complete.jar"
    
    if jar_path.exists():
        print(f"✓ ANTLR4 JAR encontrado em {jar_path}")
        return str(jar_path)
    
    print(f"Baixando ANTLR4 de https://www.antlr.org/download/...")
    import urllib.request
    url = "https://www.antlr.org/download/antlr-4.13.0-complete.jar"
    urllib.request.urlretrieve(url, jar_path)
    print(f"✓ ANTLR4 JAR baixado para {jar_path}")
    return str(jar_path)

def generate_antlr_code(grammar_path, output_dir, jar_path):
    """Gera código Python a partir da gramática ANTLR4."""
    
    # Normalizar caminhos
    grammar_path = Path(grammar_path).resolve()
    output_dir = Path(output_dir).resolve()
    
    # Criar diretório de saída se não existir
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if not grammar_path.exists():
        print(f"✗ Erro: Arquivo de gramática não encontrado: {grammar_path}")
        return False
    
    print(f"Gerando código ANTLR4 a partir de {grammar_path}...")
    print(f"Diretório de saída: {output_dir}")
    
    cmd = [
        "java",
        "-jar", jar_path,
        "-Dlanguage=Python3",
        "-visitor",
        "-o", str(output_dir),
        str(grammar_path)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("✓ Código ANTLR4 gerado com sucesso!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Erro ao gerar código ANTLR4:")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False

def main():
    """Função principal."""
    script_dir = Path(__file__).parent.resolve()
    grammar_path = script_dir / "grammar" / "MiniLang.g4"
    output_dir = script_dir / "src" / "generated"
    
    print("=" * 60)
    print("Gerador de Código ANTLR4 para MiniLang")
    print("=" * 60)
    
    # Baixar JAR
    jar_path = download_antlr_jar()
    
    # Gerar código
    success = generate_antlr_code(grammar_path, output_dir, jar_path)
    
    if success:
        # Criar __init__.py no diretório generated
        init_file = output_dir / "__init__.py"
        init_file.write_text("")
        print(f"✓ Criado {init_file}")
        
        print("\n" + "=" * 60)
        print("Geração completada com sucesso!")
        print("Arquivos gerados em:", output_dir)
        print("=" * 60)
        return 0
    else:
        print("\n" + "=" * 60)
        print("Erro na geração. Tente manualmente:")
        print(f"antlr4 -Dlanguage=Python3 -visitor -o {output_dir} {grammar_path}")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
