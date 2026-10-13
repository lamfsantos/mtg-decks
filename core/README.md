# MTG Decks - Core & Vision Lab

Módulo em Python contendo:
1. **`scryfall/`**: Cliente e utilitários da Scryfall API (preços, buscas multilíngues e bulk data).
2. **`vision/`**: Laboratório de OpenCV para detecção de cartas físicas e extração de ROIs.
3. **`api/`**: Serviço FastAPI que atende o aplicativo mobile Flutter.

## Como Executar

### 1. Criar ambiente virtual e instalar dependências
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r core/requirements.txt
```

### 2. Testar o cliente Scryfall
```bash
python3 core/scryfall/client.py
```

### 3. Iniciar a API local
```bash
uvicorn core.api.main:app --reload --port 8000
```
Acesse a documentação interativa Swagger em: `http://localhost:8000/docs`
