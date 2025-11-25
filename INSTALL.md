# Guia de Instalação Rápida - MiniLang Compiler

## Pré-requisitos

- Python 3.8+
- Java (JDK ou JRE 8+)

## Passos para Instalação

### 1. Instalar dependências Python

```bash
pip install antlr4-python3-runtime
```

### 2. Gerar código ANTLR4

```bash
# Executar o script gerador (baixa o JAR automaticamente)
python generate_antlr.py
```

Ou, se você já tem o `antlr4` instalado:

```bash
antlr4 -Dlanguage=Python3 -visitor -o src/generated grammar/MiniLang.g4
```

### 3. Verificar instalação

```bash
python -m src.cli tests/ok_simple.min
```

Você deve ver a saída:
```
=== Compilando tests/ok_simple.min ===
[1/5] Análise Léxica e Sintática...
[2/5] Construção da AST...
[3/5] Análise Semântica...
...
30
1
=== COMPILAÇÃO BEM-SUCEDIDA ===
```

## Instalação do ANTLR4 (Métodos Alternativos)

### Opção 1: Via Python Script (Recomendado)
```bash
python generate_antlr.py
```
Este script baixa automaticamente o ANTLR4 JAR se não existir.

### Opção 2: Manual com Java
1. Baixar em: https://www.antlr.org/download/antlr-4.13.0-complete.jar
2. Salvar em: `tools/antlr-4.13.0-complete.jar`
3. Executar: 
```bash
java -jar tools/antlr-4.13.0-complete.jar -Dlanguage=Python3 -visitor -o src/generated grammar/MiniLang.g4
```

### Opção 3: Chocolatey (Windows)
```powershell
choco install antlr4
antlr4 -Dlanguage=Python3 -visitor -o src/generated grammar/MiniLang.g4
```

### Opção 4: Homebrew (macOS)
```bash
brew install antlr
antlr4 -Dlanguage=Python3 -visitor -o src/generated grammar/MiniLang.g4
```

### Opção 5: apt (Linux/Debian)
```bash
sudo apt-get install antlr4
antlr4 -Dlanguage=Python3 -visitor -o src/generated grammar/MiniLang.g4
```

## Troubleshooting

### Erro: "antlr4: command not found"
- Use `python generate_antlr.py` em vez de executar `antlr4` diretamente

### Erro: "java: command not found"
- Instale Java (JDK 8+)
- No Windows: https://www.oracle.com/java/technologies/downloads/
- No macOS: `brew install openjdk`
- No Linux: `sudo apt-get install default-jdk`

### Erro: ModuleNotFoundError: No module named 'antlr4'
```bash
pip install antlr4-python3-runtime
```

## Próximos Passos

Veja `README.md` para uso do compilador.
