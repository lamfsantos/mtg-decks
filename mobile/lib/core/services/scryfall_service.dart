import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/card_model.dart';

class ScryfallService {
  static const String baseUrl = 'https://api.scryfall.com';

  // TODO(Fase 3): Implementar busca por nome e parsing para CardModel
  Future<CardModel?> searchCardNamed(String name, {bool fuzzy = true}) async {
    final uri = Uri.parse('$baseUrl/cards/named?${fuzzy ? 'fuzzy' : 'exact'}=${Uri.encodeComponent(name)}');
    final response = await http.get(uri);

    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      return CardModel(
        id: data['id'],
        name: data['name'],
        setCode: data['set'],
        setName: data['set_name'],
        collectorNumber: data['collector_number'],
        priceUsd: double.tryParse(data['prices']?['usd'] ?? ''),
        priceUsdFoil: double.tryParse(data['prices']?['usd_foil'] ?? ''),
        imageUrl: data['image_uris']?['normal'],
      );
    }
    return null;
  }
}
