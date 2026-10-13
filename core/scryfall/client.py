"""
Cliente moderno da Scryfall API.
Substitui a biblioteca legada mtgsdk com suporte a busca rápida,
cartas em português, edições e cotações de preços (USD/EUR).
"""

from typing import Any, Dict, List, Optional
import json
import urllib.parse
import urllib.request


class ScryfallClient:
    BASE_URL = "https://api.scryfall.com"

    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.headers = {
            "User-Agent": "MTGDecksApp/1.0",
            "Accept": "application/json;q=0.9,*/*;q=0.8",
        }

    def _get(self, endpoint: str, params: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        url = f"{self.BASE_URL}{endpoint}"
        if params:
            url += f"?{urllib.parse.urlencode(params)}"

        req = urllib.request.Request(url, headers=self.headers)
        with urllib.request.urlopen(req, timeout=self.timeout) as response:
            return json.loads(response.read().decode("utf-8"))

    def get_card_named(self, name: str, fuzzy: bool = True, set_code: Optional[str] = None) -> Dict[str, Any]:
        """Busca uma carta pelo nome exato ou aproximado."""
        params = {"fuzzy" if fuzzy else "exact": name}
        if set_code:
            params["set"] = set_code
        return self._get("/cards/named", params)

    def search_cards(self, query: str) -> List[Dict[str, Any]]:
        """Executa busca com sintaxe avançada da Scryfall (ex: lang:pt, set:neo, etc)."""
        data = self._get("/cards/search", {"q": query})
        return data.get("data", [])

    def search_portuguese(self, card_name: str) -> List[Dict[str, Any]]:
        """Busca carta pelo nome em português ou inglês trazendo versão localizada."""
        query = f'lang:pt "{card_name}"'
        try:
            return self.search_cards(query)
        except Exception:
            # Fallback para busca normal caso a busca em PT não localize
            return self.search_cards(card_name)

    # TODO(Fase 1): Implementar download e streaming do dump bulk data (default-cards.json)
    def download_bulk_data(self, target_path: str) -> None:
        """
        TODO: Baixar o arquivo default-cards.json da Scryfall para indexação offline.
        Endpoint: /bulk-data/default-cards
        """
        raise NotImplementedError("Download de bulk data será implementado na Fase 1.")


if __name__ == "__main__":
    client = ScryfallClient()

    print("=== Testando Scryfall API ===")
    
    # 1. Teste carta em inglês com preços
    card_en = client.get_card_named("Liliana of the Veil")
    print(f"\nNome: {card_en['name']}")
    print(f"Edição: {card_en['set_name']} ({card_en['set'].upper()})")
    print(f"Preço USD: ${card_en['prices'].get('usd')}")
    print(f"Preço USD Foil: ${card_en['prices'].get('usd_foil')}")

    # 2. Teste carta em português
    print("\nBuscando carta em PT-BR ('Supervisor Inspirador')...")
    cards_pt = client.search_portuguese("Supervisor Inspirador")
    if cards_pt:
        first = cards_pt[0]
        print(f"Nome Original: {first['name']}")
        print(f"Nome Impresso: {first.get('printed_name')}")
        print(f"Edição: {first['set'].upper()} #{first['collector_number']}")
