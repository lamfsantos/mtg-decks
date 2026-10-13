class CardModel {
  final String id;
  final String name;
  final String? printedName;
  final String setCode;
  final String setName;
  final String collectorNumber;
  final double? priceUsd;
  final double? priceUsdFoil;
  final String? imageUrl;
  final int quantity;
  final bool isFoil;
  final String condition; // NM, SP, MP, HP

  const CardModel({
    required this.id,
    required this.name,
    this.printedName,
    required this.setCode,
    required this.setName,
    required this.collectorNumber,
    this.priceUsd,
    this.priceUsdFoil,
    this.imageUrl,
    this.quantity = 1,
    this.isFoil = false,
    this.condition = 'NM',
  });

  // TODO(Fase 3): Implementar fromJson, toJson e persistência local (SQLite/Drift)
}
