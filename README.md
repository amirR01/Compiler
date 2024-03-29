# Compiler
C-minus language compiler with python

## Compiler structure
```

      (C-minus code)
            ↓
| -----------------------|
|         Scanner        |
| -----------------------|
            ↓
         (tokens)
            ↓
| -----------------------|
|         Parser         |
| -----------------------|
            ↓
      (syntax tree)
            ↓
| -----------------------|
|         CodeGen        |
| -----------------------|
            ↓
      (assembly code)
            ↓
```