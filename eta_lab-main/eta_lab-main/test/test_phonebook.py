from src.phonebook import Phonebook

class TestPhonebook:

    # Testando adição corretamente
    def test_add_correto(self):
        phonebook = Phonebook()
        result = phonebook.add("Denis", "123456789")
        resultado_esperado = "Numero adicionado"
        assert result == resultado_esperado

    # Testando adição com nome de #
    def test_add_jogovelha(self):
        phonebook = Phonebook()
        result = phonebook.add("#", "123456789")
        resultado_esperado = "Nome invalido"
        assert result == resultado_esperado

    # Testando adição com nome de @
    def test_add_arroba(self):
        phonebook = Phonebook()
        result = phonebook.add("@", "123456789")
        resultado_esperado = "Nome invalido"                #erro de codigo fonte (divida tecnica)
        assert result == resultado_esperado

    # Testando adição com nome de !
    def test_add_exclamacao(self):
        phonebook = Phonebook()
        result = phonebook.add("!", "123456789")
        resultado_esperado = "Nome invalido"
        assert result == resultado_esperado

    # Testando adição com nome de $
    def test_add_cifrao(self):
        phonebook = Phonebook()
        result = phonebook.add("$", "123456789")
        resultado_esperado = "Nome invalido"                #erro de codigo fonte (divida tecnica)
        assert result == resultado_esperado

    # Testando adição com nome de %
    def test_add_porcentagem(self):
        phonebook = Phonebook()
        result = phonebook.add("%", "123456789")
        resultado_esperado = "Nome invalido"
        assert result == resultado_esperado

    # Testando adição com quantitativo numerico errado
    def test_add_numerico_errado(self):
        phonebook = Phonebook()
        result = phonebook.add("Denis", "")                 #erro de codigo fonte - verificação (DT)
        resultado_esperado = "Numero invalido"              #erro de codigo fonte - texto (DT)
        assert result == resultado_esperado

    # Testando nomes iguais
    def test_add_nomes_iguais(self):
        phonebook = Phonebook()
        result1 = phonebook.add("Denis", "888888888888")
        result2 = phonebook.add("Helena", "777777777777")
        result3 = phonebook.add("Denis", "888888888888")
        result4 = phonebook.add("Anderson", "66666666666")

        #lista = phonebook.get_names()
        #print(lista)

        resultado_esperado = 'Contato ja existe'             #erro de codigo fonte - Texto errado/corrigido
        assert result3 == resultado_esperado

    def test_lookup_fail(self):
        phonebook = Phonebook()

        nome_verificado = phonebook.lookup("#")
        resultado_esperado = "Nome invalido"

        assert resultado_esperado == nome_verificado

    def test_lookup_passed(self):
        phonebook = Phonebook()
        result1 = phonebook.add("Denis", "888888888888")
        result2 = phonebook.add("Helena", "777777777777")

        nome_verificado = "Denis"
        numero_verificado = "888888888888"
        verificar = phonebook.lookup(nome_verificado)

        assert verificar == f"Nome: {nome_verificado}, Número: {numero_verificado}"

    def test_get_names(self):
        phonebook = Phonebook()
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")
        pessoa3 = phonebook.add("Anderson", "66666666666")

        lista = phonebook.get_names()
        print(lista)

    def test_get_numbers(self):
        phonebook = Phonebook()
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")
        pessoa3 = phonebook.add("Anderson", "66666666666")

        lista = phonebook.get_numbers()
        print(lista)

    def test_clear(self):
        phonebook = Phonebook()
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")
        pessoa3 = phonebook.add("Anderson", "66666666666")

        limpeza = phonebook.clear()
        assert limpeza == "phonebook limpado"

    def test_search(self):
        phonebook = Phonebook()
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")
        pessoa3 = phonebook.add("Anderson", "66666666666")
        pessoa4 = phonebook.add("Andersen", "55555555555")

        #busca = phonebook.search(pessoa)
        #print(busca)

        result = phonebook.search("Denis")

        expected_result = [{"Denis", "888888888888"}]
        assert result == expected_result

    def test_search_fail(self):
        phonebook = Phonebook()
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")
        pessoa3 = phonebook.add("Anderson", "66666666666")
        pessoa4 = phonebook.add("Andersen", "55555555555")

        #busca = phonebook.search(pessoa)
        #print(busca)

        result = phonebook.search("Maria")

        expected_result = []
        assert result == expected_result

    def test_get_phonebook_sorted(self):
        phonebook = Phonebook()
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")
        pessoa3 = phonebook.add("Anderson", "66666666666")
        pessoa4 = phonebook.add("Andersen", "55555555555")

        result = phonebook.get_phonebook_sorted()

        expected_result = {'Andersen': '55555555555', 'Anderson': '66666666666', 'Denis': '888888888888', 'Helena': '777777777777', 'POLICIA': '190'}
        assert result == expected_result

    def test_get_phonebook_reverse(self):
        phonebook = Phonebook()
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")
        pessoa3 = phonebook.add("Anderson", "66666666666")
        pessoa4 = phonebook.add("Andersen", "55555555555")

        result = phonebook.get_phonebook_reverse()

        expected_result = {'POLICIA': '190', 'Helena': '777777777777', 'Denis': '888888888888', 'Anderson': '66666666666', 'Andersen': '55555555555'}
        assert result == expected_result

    def test_delete(self):
        phonebook = Phonebook()
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")
        pessoa3 = phonebook.add("Anderson", "66666666666")
        pessoa4 = phonebook.add("Andersen", "55555555555")

        usuario = "Denis"

        result = phonebook.delete(usuario)

        #print(result)
        #print(phonebook.get_phonebook_sorted())

        assert result == 'Numero deletado'

    def test_delete_fail(self):
        phonebook = Phonebook()
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")
        pessoa3 = phonebook.add("Anderson", "66666666666")
        pessoa4 = phonebook.add("Andersen", "55555555555")

        usuario = "Juquinha"

        result = phonebook.delete(usuario)

        #print(result)
        #print(phonebook.get_phonebook_sorted())

        assert result == "Pessoa nao encontrada"

    def test_change_number(self):
        phonebook = Phonebook()
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")
        pessoa3 = phonebook.add("Anderson", "66666666666")
        pessoa4 = phonebook.add("Andersen", "55555555555")

        usuario = "Denis"
        novo_numero = "000000000000"

        result = phonebook.change_number(usuario, novo_numero)

        assert result == 'Numero Alterado'

    def test_change_number_fail(self):
        phonebook = Phonebook()
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")
        pessoa3 = phonebook.add("Anderson", "66666666666")
        pessoa4 = phonebook.add("Andersen", "55555555555")

        usuario = "Mauricio"
        novo_numero = "000000000000"

        result = phonebook.change_number(usuario, novo_numero)

        assert result == "Pessoa nao encontrada"


    def test_get_name_by_number_success(self):
        phonebook = Phonebook()
        phonebook.add("Carlos", "123456789")
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")

        expected = "Carlos"

        result = phonebook.get_name_by_number("123456789")

        assert result == expected

    def test_get_name_by_number_not_found(self):
        phonebook = Phonebook()
        phonebook.add("Carlos", "123456789")
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")

        result = phonebook.get_name_by_number("987654321")
        expected = "Numero não encontrado"

        assert result == expected

    def test_get_name_by_number_empty_phonebook(self):
        phonebook = Phonebook()
        result = phonebook.get_name_by_number("123456789")
        pessoa1 = phonebook.add("Denis", "888888888888")
        pessoa2 = phonebook.add("Helena", "777777777777")

        expected = "Numero não encontrado"

        assert result == expected







