# MiniLang Compiler - Opção 2 (ANTLR4 + Python)

## Visão Geral

Compilador para a linguagem **MiniLang**, implementado usando **ANTLR4** para análise léxica e sintática, e **Python 3** para análise semântica, interpretação e geração de código.

## Estrutura do Projeto

```
.
├── grammar/
│   └── MiniLang.g4          # Especificação ANTLR4 da linguagem
├── src/
│   ├── __init__.py          # Marcador de pacote
│   ├── ast_nodes.py         # Definição dos nós da AST
│   ├── sema.py              # Análise semântica
│   ├── interp.py            # Interpretador
│   ├── codegen.py           # Gerador de código Python
│   ├── pretty.py            # Impressora de AST
│   ├── ast_builder.py       # Construtor de AST (visitor ANTLR)
│   ├── cli.py               # Interface de linha de comando
│   └── generated/           # Código gerado pelo ANTLR4 (criado automaticamente)
├── tests/
│   ├── ok_geral.min         # Programa completo bem-formado
│   ├── ok_simple.min        # Programa simples bem-formado
│   ├── err_sema_type.min    # Erro semântico: tipo incompatível
│   ├── err_sema_undeclared.min  # Erro semântico: variável não declarada
│   └── err_sema_const.min   # Erro semântico: atribuição a const
└── README.md                # Este arquivo
```

## Características da Linguagem

### Tipos Básicos
- `int` - números inteiros
- `bool` - valores booleanos (`true`, `false`)
- Arrays: `int[]`, `bool[]`

### Palavras-chave
- Controle de fluxo: `if`, `else`, `while`, `do`
- Declarações: `const`, `new`
- I/O: `print`

### Operadores
| Operador | Tipo | Exemplo |
|----------|------|---------|
| `+`, `-`, `*`, `/` | Aritmético | `x + y` |
| `<`, `<=`, `==`, `!=` | Relacional | `x < 10` |
| `\|\|`, `&&` | Lógico | `a && b` |
| `!` | Negação | `!condition` |
| `=` | Atribuição | `x = 5` |

### Recursos
- **Escopo**: Blocos delimitados por `{...}` criam novos escopos
- **Shadowing**: Variáveis em escopo aninhado podem sombrear nomes externos
- **Const**: Variáveis declaradas como `const` não podem ser reatribuídas
- **Arrays**: Suportam arrays unidimensionais com verificação de limites
- **Comentários**: `// comentário de linha` e `/* comentário de bloco */`

## Fases do Compilador

1. **Análise Léxica** (ANTLR4 Lexer): Tokenização do código-fonte
2. **Análise Sintática** (ANTLR4 Parser): Construção da árvore de parse
3. **Construção da AST** (Visitor): Conversão para AST customizada
4. **Análise Semântica**: Verificação de tipos, escopos, validações
5. **Interpretação**: Execução direta da AST
6. **Geração de Código**: Conversão da AST para Python executável

## Instalação

### Pré-requisitos
- Python 3.8+
- ANTLR4 (ferramenta de linha de comando)
- pip (gerenciador de pacotes Python)

### Passos de Instalação

#### 1. Instalar o runtime ANTLR4 para Python
```bash
pip install antlr4-python3-runtime
```

#### 2. Instalar a ferramenta ANTLR4 (Windows)
Opção A - Via Chocolatey:
```powershell
choco install antlr4
```

Opção B - Download manual:
1. Baixar em: https://www.antlr.org/download/antlr-4.13.0-complete.jar
2. Configurar variável de ambiente `ANTLR_JAR` ou instalar via gerenciador

#### 3. Gerar código ANTLR4
```bash
antlr4 -Dlanguage=Python3 -visitor -o src/generated grammar/MiniLang.g4
```

Este comando cria:
- `src/generated/MiniLangLexer.py`
- `src/generated/MiniLangParser.py`
- `src/generated/MiniLangVisitor.py`

## Uso

### Execução Básica
```bash
python src/cli.py tests/ok_simple.min
```

**Saída esperada:**
```
[LEXING] Tokenizando arquivo...
[PARSING] Analisando sintaxe...
[AST BUILDING] Construindo árvore sintática...
[SEMANTIC] Analisando semântica...
[INTERPRETATION] Executando programa...

--- AST ---
Program
  Block
    Decl(x, int, 10)
    Decl(y, int, 20)
    Print(Ari(+, Id(x), Id(y)))
    Print(Rel(<, Id(x), Id(y)))

--- SYMBOL TABLE ---
x: {type: int, const: False, init: True, value: 10}
y: {type: int, const: False, init: True, value: 20}

--- INTERPRETER OUTPUT ---
30
1
```

### Gerar Código Python
```bash
python src/cli.py tests/ok_simple.min --codegen
```

Mostra o código Python gerado equivalente ao programa MiniLang.

### Modo Trace (Debug)
```bash
python src/cli.py tests/ok_geral.min --trace
```

Mostra informações detalhadas de cada fase.

### Gerar Código ANTLR
```bash
python src/cli.py --generate-antlr
```

Executa a geração automática do código ANTLR4.

## Exemplos de Programas

### Exemplo 1: Programa Simples
```minilang
{
  int x = 5;
  int y = 10;
  print(x + y);           // Saída: 15
  print(x < y);           // Saída: 1 (true)
}
```

### Exemplo 2: Arrays
```minilang
{
  const int N = 3;
  int[] arr = new int[N];
  
  arr[0] = 10;
  arr[1] = 20;
  arr[2] = 30;
  
  print(arr[0], arr[1], arr[2]);  // Saída: 10 20 30
}
```

### Exemplo 3: Controle de Fluxo
```minilang
{
  int i = 0;
  
  while (i < 3) {
    print(i);
    i = i + 1;
  }
  
  // Saída:
  // 0
  // 1
  // 2
}
```

### Exemplo 4: Const e Shadowing
```minilang
{
  const int X = 5;
  print(X);           // Saída: 5
  
  {
    int X = 10;       // Novo escopo, novo X
    print(X);         // Saída: 10
  }
  
  print(X);           // Saída: 5 (volta ao X original)
}
```

## Testes

### Executar Arquivo de Teste
```bash
# Teste bem-formado
python src/cli.py tests/ok_simple.min

# Teste com erro semântico
python src/cli.py tests/err_sema_type.min
```

### Testes Disponíveis

| Arquivo | Descrição |
|---------|-----------|
| `ok_simple.min` | Programa simples: aritmética e comparação |
| `ok_geral.min` | Programa completo: arrays, const, scoping, control flow |
| `err_sema_type.min` | Erro: operação com tipos incompatíveis |
| `err_sema_undeclared.min` | Erro: variável não declarada |
| `err_sema_const.min` | Erro: tentativa de modificar variável const |

## Estrutura do Código

### `ast_nodes.py` - Nós da AST
Defines dataclasses para todos os tipos de nós:
- Statements: `Decl`, `Eval`, `Print`, `If`, `While`, `Do`, `Assign`
- Expressions: `Rel`, `Eq`, `Lg`, `Unary`, `Ari`, `ArrayRef`, `NewArray`, `Num`, `Bool`, `Id`

### `sema.py` - Análise Semântica
- Gerenciamento de escopo com pilha de símbolos
- Inferência de tipos
- Verificação de def-use (uso antes da definição)
- Validação de const
- Detecção de erros semânticos

### `interp.py` - Interpretador
- Execução direta da AST
- Pilha de frames para escopos
- Avaliação de expressões
- Execução de statements
- Verificação de limites de arrays em tempo de execução

### `codegen.py` - Gerador de Código
- Converte AST para código Python executável
- Mantém estrutura de frames para escopo
- Gera código de verificação de limites
- Preserva semântica de const

### `pretty.py` - Impressora de AST
- Imprime AST em formato ASCII tree
- Mostra rótulos descritivos
- Formata com caracteres de desenho de caixa

### `ast_builder.py` - Construtor de AST
- Implementa pattern Visitor do ANTLR4
- Converte árvore de parse para AST customizada
- Trata operadores e precedência

### `cli.py` - Interface de Linha de Comando
- Orquestra todas as 5 fases do compilador
- Suporta opções: `--trace`, `--codegen`, `--generate-antlr`
- Trata erros em cada fase
- Exibe saídas estruturadas

## Tratamento de Erros

### Erros Sintáticos
Detectados pelo parser ANTLR4:
```
line 5:8: no viable alternative at input 'print'
```

### Erros Semânticos
Detectados pela análise semântica:
```
SemanticError: Variable 'x' is not declared (line 3)
SemanticError: Type mismatch in operation + (int + bool) (line 5)
SemanticError: Cannot assign to const variable 'N' (line 7)
```

### Erros de Runtime
Detectados durante interpretação:
```
RuntimeErrorLang: Array index out of bounds (line 10)
```

## Modificando a Gramática

Para adicionar novas construções à linguagem:

1. Editar `grammar/MiniLang.g4`
2. Executar: `antlr4 -Dlanguage=Python3 -visitor -o src/generated grammar/MiniLang.g4`
3. Atualizar métodos correspondentes em:
   - `ast_builder.py` (novo visitMethod)
   - `ast_nodes.py` (novo dataclass se necessário)
   - `sema.py` (validação semântica)
   - `interp.py` (execução)
   - `codegen.py` (geração de código)
   - `pretty.py` (impressão)

## Referências

- **ANTLR4**: https://www.antlr.org/
- **Python ANTLR Runtime**: https://pypi.org/project/antlr4-python3-runtime/
- **Repositório de Referência**: https://github.com/RcFarah/A2-Compiladores

## Licença

Trabalho acadêmico - Universidade Federal
