from .codesniffer_class import Sniffer as Sniffer_ai
BATCH_SIZE = 16
WORKERS = 4
NUM_LABELS=8
MODEL_PATH = "static/trained_model/codeSniffer.pth"
class Sniffer:
    def CodeAnalysis(self, jcode):

        model_pth = Sniffer_ai(MODEL_PATH)
        result = model_pth.CodeAnalysis(jcode)
        return result

Sniffer = Sniffer()

