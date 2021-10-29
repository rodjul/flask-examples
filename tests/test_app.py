import unittest
import json

try:
    from app import app
except ModuleNotFoundError:
    from app.app import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        '''
        Antes de iniciar os tests, configuramos o flask informando que será testado a aplicação
        '''
        self.app = app.test_client()
    
    def tearDown(self):
        '''
        Se precisar remover algum valor, ao executar todos os tests será executado essa função por último
        '''
        print("Finished")

    def test_api_hello(self):
        page = self.app.get("/api/world/json1")
        response = json.loads(page.get_data())
        self.assertEqual(page.status_code, 200, "O valor esperado para o index é 200")
        self.assertEqual(response['message'], "Hello world", "A api não retornou uma mensagem dinâmica")
    
    def test_get_index(self):
        home = self.app.get("/")
        self.assertEqual(home.status_code, 200, "O valor esperado para o index é 200")
        self.assertEqual(home.get_data(as_text=True), "<p>Hello World!</p>", "O valor do index, deveria ser <p>Hello, World!</p>")
    


if __name__ == "__main__":
    unittest.main()
