from IACode.sniffer import Sniffer
def test_sniffer():
    code_analysis_result = Sniffer.CodeAnalysis("some code sample")
    for d in code_analysis_result:
        print(f'{d}: {code_analysis_result[d]}')

if __name__ == "__main__":
    test_sniffer()
    print("Everything passed")