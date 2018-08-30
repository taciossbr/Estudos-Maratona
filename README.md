



## AD-HOC

### Binarios em Python

#### Operadores Binario em Python

- `x << b` retorna `x` com `y` casas á esquerda. Ex.:
  ```python
  14 << 9 # decimal 7168
  1110 << 1001 # binario 1110000000000
  ```
  - O mesmo que $`x(2^y)`$
- `x >> b` retorna `x` com `y` casas á direita. Ex.:
  ```python
  14 >> 9 # decimal 0 2 >> 1 #decimal 1
  1110 >> 1001 # binario 0 10 >> 1 # binario 1
  ```
  - O mesmo que $`\frac{x}{2^y},\ com\ x, y \in \mathbb{Z}`$
- `x & y` realiza um `AND` binario.
- `x | y` realiza um `OR` binario.
- `x ^ y` realiza um `xOR` binario.
- `~x` retorna o complemento, `NOT`