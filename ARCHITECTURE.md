# Arquitetura do MiniLang Compiler - Opção 2

## Visão Geral da Arquitetura

```
┌─────────────────┐
│  Arquivo .min   │
│  (Código-fonte) │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│   Análise Léxica (ANTLR4)   │ ← MiniLangLexer.py (gerado)
├─────────────────────────────┤
│  Tokenização, reconhecimento │
│  de palavras-chave, operadores│
└─────────────┬───────────────┘
              │
              ▼
    ┌────────────────────┐
    │   Token Stream     │
    └─────────┬──────────┘
              │
              ▼
┌─────────────────────────────┐
│   Análise Sintática (ANTLR4)│ ← MiniLangParser.py (gerado)
├─────────────────────────────┤
│  Reconhecimento de gramática│
│  Construção de Parse Tree   │
└─────────────┬───────────────┘
              │
              ▼
    ┌────────────────────┐
    │   Parse Tree       │
    │   (ANTLR)          │
    └─────────┬──────────┘
              │
              ▼
┌─────────────────────────────┐
│  Construção da AST (Python) │ ← ast_builder.py
├─────────────────────────────┤
│  Visitor Pattern (ANTLR)    │
│  Conversão para AST custom  │
│  Definido em ast_nodes.py   │
└─────────────┬───────────────┘
              │
              ▼
    ┌────────────────────┐
    │  AST Customizada   │
    │  (Nossos tipos)    │
    └─────────┬──────────┘
              │
              ▼
┌─────────────────────────────┐
│  Análise Semântica (Python) │ ← sema.py
├─────────────────────────────┤
│  ✓ Type Checking            │
│  ✓ Scope Management         │
│  ✓ Def-Use Analysis         │
│  ✓ Const Validation         │
│  ✓ Error Reporting          │
└─────────────┬───────────────┘
              │
              ├─────────────────────────┐
              │                         │
              ▼                         ▼
   ┌──────────────────┐    ┌───────────────────┐
   │ Symbol Table     │    │ Erros Detectados? │
   └──────────────────┘    │ (SemanticError)   │
                           └───────────────────┘
              │
              ▼
   ┌──────────────────┐
   │  AST Validado    │
   └────────┬─────────┘
            │
            ├────────────────────────┐
            │                        │
            ▼                        ▼
  ┌──────────────────┐    ┌─────────────────┐
  │ Interpretação    │    │ Geração de      │
  │ (interp.py)      │    │ Código Python   │
  │                  │    │ (codegen.py)    │
  │ • Execução direta│    │                 │
  │   da AST         │    │ • Tradução para │
  │ • Frame stack    │    │   código Python │
  │   para escopos   │    │ • Preserva      │
  │ • Runtime checks │    │   semântica     │
  └────────┬─────────┘    └────────┬────────┘
           │                       │
           ▼                       ▼
  ┌──────────────────┐    ┌─────────────────┐
  │ STDOUT Output    │    │ Código Python   │
  │ (Interpretado)   │    │ Executável      │
  └──────────────────┘    └────────┬────────┘
                                   │
                                   ▼
                          ┌─────────────────┐
                          │ Exec Código     │
                          │ Python Gerado   │
                          └────────┬────────┘
                                   │
                                   ▼
                          ┌─────────────────┐
                          │ STDOUT Output   │
                          │ (Do codegen)    │
                          └─────────────────┘
```

## Componentes do Projeto

### 1. **grammar/MiniLang.g4**
- **Tipo**: Especificação ANTLR4
- **Responsabilidade**: Define a sintaxe completa de MiniLang
- **Lexer**: Tokens (IF, WHILE, DO, PRINT, operadores, etc.)
- **Parser**: Regras gramaticais (program, block, stmt, expr, etc.)
- **Precedência**: Operadores bem definidos com associatividade correta

### 2. **src/generated/** (Gerado automaticamente)
- **MiniLangLexer.py**: Lexer gerado pelo ANTLR4
- **MiniLangParser.py**: Parser gerado pelo ANTLR4
- **MiniLangVisitor.py**: Classe base Visitor do ANTLR4
- **Outros**: Arquivos auxiliares (.interp, .tokens)

### 3. **src/ast_nodes.py**
- **Tipo**: Definições de tipos Python (dataclasses)
- **Responsabilidade**: Define todos os nós da AST
- **Nós suportados**:
  - Program, Block
  - Decl (declarações com const support)
  - Eval (expressão como statement)
  - Print (output)
  - If, While, Do (control flow)
  - Assign (atribuição)
  - Expressões: Rel, Eq, Lg, Unary, Ari, NewArray, ArrayRef, Num, Bool, Id

### 4. **src/ast_builder.py**
- **Tipo**: Visitor do ANTLR4 customizado
- **Responsabilidade**: Converte ParseTree (ANTLR) → AST (nossos tipos)
- **Padrão**: Visitor pattern
- **Métodos**: visitProgram, visitBlock, visitStmt, visitExpr, etc.
- **Tratamento**: Operadores, arrays, precedência

### 5. **src/sema.py**
- **Tipo**: Analisador semântico
- **Responsabilidade**: Validação semântica completa
- **Features**:
  - Type inference automática
  - Scope management com pilha de símbolos
  - Def-use analysis (uso antes da definição)
  - Const validation (não permite reatribuição)
  - Error reporting específico
- **Output**: Symbol table (dicionário de símbolos por escopo)

### 6. **src/interp.py**
- **Tipo**: Interpretador direto de AST
- **Responsabilidade**: Executa o programa
- **Features**:
  - Frame stack para gerenciar escopos
  - Avaliação recursiva de expressões
  - Verificação de limites de array em runtime
  - Conversão de booleanos para 0/1 em print
- **Output**: Saída padrão (stdout)

### 7. **src/codegen.py**
- **Tipo**: Gerador de código Python
- **Responsabilidade**: Traduz AST → Código Python executável
- **Features**:
  - Geração de código legível
  - Preservação de semântica de const
  - Frame stack para escopos
  - Conversão de booleanos para 0/1 em print
- **Output**: String contendo função `__ml_run(env)`

### 8. **src/pretty.py**
- **Tipo**: Visualizador de AST
- **Responsabilidade**: Imprime AST em formato ASCII tree
- **Features**:
  - Rótulos descritivos
  - Apenas caracteres ASCII (compatibilidade com encoding)
  - Labels de arestas opcionais
- **Output**: Árvore formatada para stdout

### 9. **src/cli.py**
- **Tipo**: Interface de linha de comando
- **Responsabilidade**: Orquestra o pipeline compilador
- **Fases**:
  1. Lexing + Parsing (ANTLR)
  2. AST Building
  3. Semantic Analysis
  4. Pretty Printing
  5. Interpretation + Code Generation
- **Opções**:
  - `--generate-antlr`: Gera código ANTLR4
  - `--trace`: Executa com debug
  - `--codegen`: Mostra código Python gerado

### 10. **generate_antlr.py**
- **Tipo**: Script auxiliar
- **Responsabilidade**: Gera código ANTLR4 automaticamente
- **Features**:
  - Download automático do ANTLR4 JAR se necessário
  - Chama ANTLR4 via Java
  - Cria __init__.py no diretório gerado

## Fluxo de Compilação

### Fase 1: Análise Léxica e Sintática
```
Arquivo.min → MiniLangLexer.py → Token Stream → MiniLangParser.py → ParseTree
```

### Fase 2: Construção da AST
```
ParseTree → ASTBuilder (Visitor) → AST Customizada
```

### Fase 3: Análise Semântica
```
AST → sema.check_semantics() → { Validações, Symbol Table, Erros? }
```

### Fase 4: Visualização (Debug)
```
AST → pretty.print_ast_ascii() → Console Output
```

### Fase 5 (Paralelo): Interpretação vs Code Generation
```
AST → interp.exec_program() → Saída Imediata (stdout)
AST → codegen.codegen_python() → Código Python → Execução → Saída
```

## Tratamento de Erros

### Erros Sintáticos
- Detectados pelo **ANTLR4 Parser**
- Exceptions padrão do ANTLR4
- Exemplos: "no viable alternative at input"

### Erros Semânticos
- Detectados por **sema.py**
- Exception personalizada: `SemanticError`
- Exemplos:
  - "Variable not declared"
  - "Type mismatch"
  - "Cannot assign to const"
  - "Array index out of bounds at compile-time"

### Erros de Runtime
- Detectados durante **interpretação**
- Exception personalizada: `RuntimeErrorLang`
- Exemplos:
  - "Array index out of bounds at runtime"
  - "Variable not found in any scope"

## Decisões de Projeto

### 1. ANTLR4 para Front-end
- ✓ Automático e confiável
- ✓ Separação clara entre sintaxe e semântica
- ✓ Fácil manutenção da gramática

### 2. Python para Back-end
- ✓ Expressividade para lógica complexa
- ✓ Fácil prototipagem
- ✓ Code generation portável

### 3. Dataclasses para AST
- ✓ Type-safe (IDE autocomplete)
- ✓ Serialização automática
- ✓ Código mais legível

### 4. Symbol Table por Escopo
- ✓ Suporte para shadowing
- ✓ Fácil gerenciar const
- ✓ Preparado para análise de def-use

### 5. Interpretador + Code Generator
- ✓ Dupla validação
- ✓ Útil para debug/educação
- ✓ Demonstra múltiplas abordagens

## Extensibilidade

### Adicionar novo tipo de statement
1. Modificar `grammar/MiniLang.g4`
2. Executar `python generate_antlr.py`
3. Adicionar `visitNewStmt()` em `ast_builder.py`
4. Adicionar dataclass em `ast_nodes.py`
5. Adicionar validação em `sema.py`
6. Adicionar execução em `interp.py`
7. Adicionar geração de código em `codegen.py`
8. Adicionar impressão em `pretty.py`

### Adicionar novo tipo de expressão
- Passos similares, mas focado em operadores

### Adicionar novo tipo base
- Adicionar ao system de tipos em `sema.py`
- Atualizar conversões de tipo

## Performance

- **Lexing/Parsing**: O(n) - linear na entrada
- **AST Building**: O(n) - visita cada nó uma vez
- **Semantic Analysis**: O(n) - análise simples, linear
- **Interpretation**: Depende do programa (loops, recursão)
- **Code Generation**: O(n) - gera código para cada nó

## Memória

- **AST em memória**: Típica mente < 100KB para programas pequenos
- **Symbol Table**: Mínima (apenas nomes e tipos)
- **Stack de frames**: Cresce com profundidade de escopo

## Compatibilidade

- Python 3.8+
- ANTLR4 runtime (any version)
- Java 8+ (para gerar código ANTLR)
