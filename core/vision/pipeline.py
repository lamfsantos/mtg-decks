"""
Laboratório de Visão Computacional (OpenCV).
Responsável por:
1. Detectar contornos retangulares da carta (proporção 1:1.4).
2. Aplicar transformação de perspectiva (Warp 4-point transform).
3. Recortar ROI do Título (topo) e Rodapé de Edição (canto inferior esquerdo).
"""

from typing import Optional, Tuple
import numpy as np


class CardVisionPipeline:
    def __init__(self, target_width: int = 630, target_height: int = 880):
        self.target_width = target_width
        self.target_height = target_height

    def preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """
        TODO(Fase 2): Aplicar Grayscale + Gaussian Blur + Canny Edge Detection
        para evidenciar as bordas externas da carta.
        """
        raise NotImplementedError("TODO: Implementar pré-processamento de bordas com OpenCV.")

    def find_card_contour(self, edges: np.ndarray) -> Optional[np.ndarray]:
        """
        TODO(Fase 2): Encontrar o maior contorno de 4 vértices cuja proporção
        seja próxima de 1:1.4 (63mm x 88mm).
        """
        raise NotImplementedError("TODO: Implementar detecção de contorno da carta.")

    def warp_perspective(self, image: np.ndarray, corners: np.ndarray) -> np.ndarray:
        """
        TODO(Fase 2): Usar cv2.getPerspectiveTransform e cv2.warpPerspective
        para desentortar a carta em um retângulo plano normalizado de 630x880px.
        """
        raise NotImplementedError("TODO: Implementar homografia / 4-point transform.")

    def extract_rois(self, warped_card: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        TODO(Fase 2): Recortar:
        - title_roi: Topo (y: 4% a 12%, x: 5% a 95%)
        - collector_roi: Rodapé inferior esquerdo (y: 92% a 97%, x: 5% a 35%)
        """
        raise NotImplementedError("TODO: Implementar recorte das regiões de interesse.")


if __name__ == "__main__":
    print("Módulo de Visão Computacional pronto para implementação na Fase 2.")
