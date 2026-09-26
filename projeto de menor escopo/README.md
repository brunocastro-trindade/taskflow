# API de recados

Projeto pequeno para aprender os fundamentos de uma API REST com Python e FastAPI.

## Objetivo

Criar uma API que permita cadastrar e listar recados. Cada recado terá um texto e um identificador numérico.

## Escopo

- `GET /recados`: listar os recados.
- `POST /recados`: cadastrar um recado.
- Dados guardados em memória enquanto o programa estiver rodando.

## Etapas de aprendizado

1. Preparar o ambiente e criar uma primeira rota `GET /`.
2. Criar a lista de recados e a rota `GET /recados`.
3. Receber e validar um recado na rota `POST /recados`.
4. Testar os dois caminhos e os casos de erro.

O código deste projeto fica nesta pasta. O `main.py` da pasta superior pertence ao exercício anterior.

## Como executar

No terminal, dentro desta pasta:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
fastapi dev main.py
```

Abra http://127.0.0.1:8000/docs para testar as rotas.