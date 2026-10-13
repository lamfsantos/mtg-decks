import 'package:flutter/material.dart';

class CollectionScreen extends StatelessWidget {
  const CollectionScreen({super.key});

  // TODO(Fase 4): Buscar lista de cartas do SQLite/Drift local e API
  // TODO(Fase 4): Exibir soma de valor em USD / BRL e filtros

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Minha Coleção MTG'),
        actions: [
          IconButton(
            icon: const Icon(Icons.file_download),
            tooltip: 'Exportar CSV',
            onPressed: () {
              // TODO(Fase 4): Exportar lista no formato CSV (ManaBox / Moxfield)
            },
          ),
        ],
      ),
      body: const Center(
        child: Text(
          'TODO: Grid de cartas catalogadas\ncom contagem, raridades e valor total.',
          textAlign: TextAlign.center,
        ),
      ),
    );
  }
}
