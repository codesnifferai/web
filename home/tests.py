from django.test import TestCase
import os
from .models import CodeSnippet, Scores
from IACode.sniffer import Sniffer
# Create your tests here.

class SimpleTest(TestCase):

    def test_index_page(self):
        print("***=== Index page get test")
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)

    def test_api(self):
        print("***=== Api Rest get test")
        response = self.client.get('/api/v1/codesnifferai/')
        self.failUnlessEqual(response.status_code, 200)

    def test_code(self):
        print("***=== Code page post test")
        directory = os.getcwd()
        # print(directory)
        java_file = open(directory + "/class2test/org.apache.oozie.command.XCommand.java", "r")

        # read whole file to a string
        data = java_file.read()

        # close file
        java_file.close()

        response = self.client.post('/code/', {'code': data})
        self.failUnlessEqual(response.status_code, 200)

    def test_ia_model(self):
        print("***=== Testing the AI model for class org.apache.oozie.command.XCommand.java (20k)")
        result_assets = {'Data Class': 0.07, 'God Class': 0.02, 'Model Class': 1.0, 'Schizofrenic Class': 0.05}
        directory = os.getcwd()
        java_file = open(directory + "/class2test/org.apache.oozie.command.XCommand.java", "r")
        code = java_file.read()
        java_file.close()

        cs = CodeSnippet()
        cs.code = code
        cs.source = "web"
        cs.save()

        try:
            code_analysis_result = Sniffer.CodeAnalysis(code)
            for d in code_analysis_result:
                print(d)
                scores = Scores()
                scores.name = d
                scores.code = cs
                scores.value = code_analysis_result[d]
                scores.save()

            result = Sniffer.CodeAnalysis(code)
            result_model = {key: result[key] for key in result if result[key] > 0}
            for key  in result_model:
                print(" Model value: {} , expected value: {}".format(result_model[key], result_assets[key]))
                self.failUnlessEqual(result_model[key], result_assets[key])

        except Exception as error:
            raise error
