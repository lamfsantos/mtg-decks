import 'package:flutter/material.dart';

class ScannerScreen extends StatefulWidget {
  const ScannerScreen({super.key});

  @override
  State<ScannerScreen> createState() => _ScannerScreenState();
}

class _ScannerScreenState extends State<ScannerScreen> {
  // TODO(Fase 3): Inicializar CameraController e Google ML Kit TextRecognizer
  // TODO(Fase 3): Implementar recorte da ROI de título e rodapé na imagem da câmera

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('MTG Card Scanner'),
        centerTitle: true,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              width: 250,
              height: 350,
              decoration: BoxDecoration(
                border: Border.all(color: Colors.blueAccent, width: 2),
                borderRadius: BorderRadius.circular(12),
              ),
              child: const Center(
                child: Text(
                  'TODO: Mira da Câmera (63x88mm)\nPreview em tempo real',
                  textAlign: TextAlign.center,
                ),
              ),
            ),
            const SizedBox(height: 24),
            ElevatedButton.icon(
              onPressed: () {
                // TODO(Fase 3): Disparar leitura e salvar na coleção
              },
              icon: const Icon(Icons.camera_alt),
              label: const Text('Escanear Carta'),
            ),
          ],
        ),
      ),
    );
  }
}
