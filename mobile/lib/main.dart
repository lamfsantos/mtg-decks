import 'package:flutter/material.dart';
import 'features/collection/collection_screen.dart';
import 'features/scanner/scanner_screen.dart';

void main() {
  runApp(const MTGDecksApp());
}

class MTGDecksApp extends StatelessWidget {
  const MTGDecksApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MTG Decks & Scanner',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        brightness: Brightness.dark,
        colorSchemeSeed: Colors.amber,
        useMaterial3: true,
      ),
      home: const MainNavigationScreen(),
    );
  }
}

class MainNavigationScreen extends StatefulWidget {
  const MainNavigationScreen({super.key});

  @override
  State<MainNavigationScreen> createState() => _MainNavigationScreenState();
}

class _MainNavigationScreenState extends State<MainNavigationScreen> {
  int _currentIndex = 0;

  final List<Widget> _screens = const [
    ScannerScreen(),
    CollectionScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_currentIndex],
      bottomNavigationBar: NavigationBar(
        selectedIndex: _currentIndex,
        onDestinationSelected: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
        destinations: const [
          NavigationDestination(
            icon: Icon(Icons.qr_code_scanner),
            selectedIcon: Icon(Icons.qr_code_scanner, color: Colors.amber),
            label: 'Scanner',
          ),
          NavigationDestination(
            icon: Icon(Icons.view_carousel_outlined),
            selectedIcon: Icon(Icons.view_carousel, color: Colors.amber),
            label: 'Coleção',
          ),
        ],
      ),
    );
  }
}
