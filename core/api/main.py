"""
API REST do MTG Decks.
Serviço para busca de cartas, precificação e sincronização da coleção.
"""

from typing import Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException, Query
from core.scryfall.client import ScryfallClient

app = FastAPI(
    title="MTG Decks Core API",
    description="API para busca de cartas, cotações e sincronização de coleção",
    version="0.1.0",
)

scryfall = ScryfallClient()


@app.get("/")
def health_check() -> Dict[str, str]:
    return {"status": "ok", "service": "mtg-decks-core"}


@app.get("/cards/named")
def get_card_named(
    name: str = Query(..., description="Nome da carta em inglês"),
    fuzzy: bool = Query(True, description="Busca aproximada"),
) -> Dict[str, Any]:
    """Busca uma carta na Scryfall pelo nome."""
    try:
        return scryfall.get_card_named(name, fuzzy=fuzzy)
    except Exception as exc:
        raise HTTPException(status_code=404, detail=f"Carta não encontrada: {str(exc)}")


@app.get("/cards/search")
def search_cards(
    q: str = Query(..., description="Query de busca (suporta sintaxe Scryfall como 'lang:pt')"),
) -> List[Dict[str, Any]]:
    """Pesquisa cartas com suporte a filtros e idiomas."""
    try:
        return scryfall.search_cards(q)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Erro na busca: {str(exc)}")


# TODO(Fase 3): Endpoints para gerenciamento da coleção
@app.get("/collection")
def list_collection():
    """TODO: Retornar cartas catalogadas do usuário."""
    return {"todo": "Listagem de cartas salvas no banco de dados."}


@app.post("/collection")
def add_card_to_collection():
    """TODO: Salvar carta na coleção com quantidade, foil e condição."""
    return {"todo": "Adição de carta à coleção."}


# TODO(Fase 2/3): Endpoint para upload e processamento de imagem
@app.post("/cards/scan")
def scan_card_image():
    """TODO: Receber imagem de carta física, processar com OpenCV e retornar candidatos."""
    return {"todo": "Processamento de imagem via OpenCV."}
