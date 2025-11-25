# Exemplos de Programas MiniLang

## Exemplo 1: FizzBuzz (Clássico)

```minilang
{
  const int N = 15;
  int i;
  i = 1;
  while (i <= N) {
    if ((i % 3 == 0) && (i % 5 == 0)) {
      print(i);  // Seria "FizzBuzz" em versão real
    } else {
      if (i % 3 == 0) {
        print(i);  // Seria "Fizz"
      } else {
        if (i % 5 == 0) {
          print(i);  // Seria "Buzz"
        } else {
          print(i);
        }
      }
    }
    i = i + 1;
  }
}
```

## Exemplo 2: Fatorial

```minilang
{
  int n;
  int result;
  n = 5;
  result = 1;
  
  while (n > 1) {
    result = result * n;
    n = n - 1;
  }
  
  print(result);  // Output: 120
}
```

## Exemplo 3: Operações com Arrays

```minilang
{
  const int SIZE = 10;
  int[] numbers = new int[SIZE];
  int i;
  int sum;
  
  // Inicializa array com números
  i = 0;
  while (i < SIZE) {
    numbers[i] = i + 1;
    i = i + 1;
  }
  
  // Soma todos os elementos
  sum = 0;
  i = 0;
  while (i < SIZE) {
    sum = sum + numbers[i];
    i = i + 1;
  }
  
  print(sum);  // Output: 55 (1+2+...+10)
}
```

## Exemplo 4: Busca em Array

```minilang
{
  const int SIZE = 5;
  int[] arr = new int[SIZE];
  int target;
  int i;
  bool found;
  
  // Inicializa array
  arr[0] = 10;
  arr[1] = 20;
  arr[2] = 30;
  arr[3] = 40;
  arr[4] = 50;
  
  target = 30;
  found = false;
  i = 0;
  
  // Busca linear
  while (i < SIZE) {
    if (arr[i] == target) {
      found = true;
    }
    i = i + 1;
  }
  
  print(found);  // Output: 1 (true)
}
```

## Exemplo 5: Escopo e Shadowing

```minilang
{
  int x;
  x = 10;
  print(x);  // Output: 10
  
  {
    int x;
    x = 20;
    print(x);  // Output: 20
    
    {
      int x;
      x = 30;
      print(x);  // Output: 30
    }
    
    print(x);  // Output: 20
  }
  
  print(x);  // Output: 10
}
```

## Exemplo 6: Operadores Lógicos

```minilang
{
  bool a;
  bool b;
  bool c;
  
  a = true;
  b = false;
  
  // AND lógico
  c = a && b;
  print(c);  // Output: 0 (false)
  
  // OR lógico
  c = a || b;
  print(c);  // Output: 1 (true)
  
  // NOT lógico
  c = !a;
  print(c);  // Output: 0 (false)
  
  // Combinações
  c = (a && !b) || b;
  print(c);  // Output: 1 (true)
}
```

## Exemplo 7: Do-While

```minilang
{
  int i;
  i = 0;
  
  do {
    print(i);
    i = i + 1;
  } while (i < 3);
  
  // Output:
  // 0
  // 1
  // 2
}
```

## Exemplo 8: Múltiplos Prints em Um Statement

```minang
{
  int x;
  int y;
  int z;
  
  x = 1;
  y = 2;
  z = 3;
  
  // Multiple args em um print
  print(x, y, z);  // Output: 1 2 3
  
  print(x + y, y * z);  // Output: 3 6
  
  print(x < y, y <= z);  // Output: 1 1
}
```

## Exemplo 9: Const Variables

```minilang
{
  const int PI_APPROX = 314;
  const int DIAMETER = 100;
  int circumference;
  
  circumference = (PI_APPROX * DIAMETER) / 100;
  print(circumference);  // Output: 314
  
  // Tentativa de modificar const gera erro semântico
  // PI_APPROX = 315;  // ERRO: Cannot assign to const
}
```

## Exemplo 10: Tratamento de Operadores

```minilang
{
  int a;
  int b;
  
  a = 10;
  b = 3;
  
  print(a + b);      // Output: 13
  print(a - b);      // Output: 7
  print(a * b);      // Output: 30
  print(a / b);      // Output: 3 (divisão inteira)
  
  print(a < b);      // Output: 0 (false)
  print(a <= b);     // Output: 0 (false)
  print(a == b);     // Output: 0 (false)
  print(a != b);     // Output: 1 (true)
  
  print(-a);         // Output: -10
  print(-(-a));      // Output: 10
}
```

## Estrutura de Teste

Para testar estes exemplos:

```bash
# Criar arquivo exemplo.min com o código
# Executar:
python -m src.cli exemplo.min

# Ver código gerado:
python -m src.cli exemplo.min --codegen

# Executar com debug:
python -m src.cli exemplo.min --trace
```

## Limitações do MiniLang

- Sem funções/procedimentos
- Sem strings (só inteiros e booleanos)
- Sem structs/records
- Sem operadores bitwise
- Sem módulo (%) ou potência (**)
- Sem for loops (apenas while/do-while)
- Sem switch/case
- Sem tipos nomeados (typedefs)
- Sem recursão (sem funções)

## Extensões Possíveis

1. **Funções**: `int func(int a, int b) { ... }`
2. **Arrays multidimensionais**: `int[][] matrix = new int[3][3];`
3. **Strings**: `string msg = "Hello";`
4. **For loops**: `for (int i = 0; i < 10; i++) { ... }`
5. **Switch/case**: `switch (x) { case 1: ... }`
6. **Operador módulo**: `a % b`
7. **Ponteiros/referências**: `int* ptr = &x;`
8. **Registros**: `struct Point { int x; int y; }`
