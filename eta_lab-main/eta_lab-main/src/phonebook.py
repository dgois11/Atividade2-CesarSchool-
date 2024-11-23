from PIL.ImImagePlugin import number
from fontTools.ttLib.tables.grUtils import entries


class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        invalid_char = {'#', '@', '!', '$', '%'}
        if any(char in name for char in invalid_char):
            return 'Nome invalido'

        '''
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nme invalido'                   # String Incorreta
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalio'                   # String Incorreta
        if '%' in name:
            return 'Nome invalido'
        '''

        if not number or not number.isdigit():
            return 'Numero invalido'

        '''
        if len(number) > 0 :                         # Verificação Incorreta (função errada)
            return 'Numero invalid'                 # String Incorreta
        '''

        if name not in self.entries:
            self.entries[name] = number                # Variavel estava number, o correto é name
            #self.entries[number] = number
            #return 'Nome invalido'                  # Não necessario - Alterar Mensagem para Numero Adicionado
            return 'Numero adicionado'

        #return 'Numero adicionado'                  # Deveria esta dentro do IF anterior
        return 'Contato ja existe'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        invalid_char = {'#', '@', '!', '$', '%'}
        if any(char in name for char in invalid_char):
            return 'Nome invalido'

        '''
        if '#' in name:
            return 'Nome invaldo'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nme invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome nvalido'
        '''

        return f"Nome: {name}, Número: {self.entries[name]}"

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """

        result = []
        for name, number in self.entries.items():           # Retirando o not da condicional
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        valor_aleatorio = dict(sorted(self.entries.items()))        #Adicionamos essa linha de codigo, que realiza o sorted

        return valor_aleatorio

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        """

        valor_reverso = dict(sorted(self.entries.items(), reverse=True))  # Adicionamos essa linha de codigo, que realiza o sorted e reverse = True

        return valor_reverso

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        if name not in self.entries:
            return "Pessoa nao encontrada"

        self.entries.pop(name)
        return 'Numero deletado'

    def change_number(self, nome, novo_numero):
        if nome not in self.entries:
            return "Pessoa nao encontrada"

        self.entries[nome] = novo_numero
        return 'Numero Alterado'

    def get_name_by_number(self, number):
        for name, num in self.entries.items():
            if num == number:
                return name

        return "Numero não encontrado"







