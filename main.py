import sqlite3


class Main:
  def __init__(self):
    self.database = sqlite3.connect('database.db')

    self.database.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL, age INTEGER NOT NULL)''')

    self.execute()

  def close_script(self, message):
    self.database.close()

    print(message)

    exit()

  def options(self):
    print('-------------------')
    print('1 - para criar um usuário')
    print('2 - para ler todos os usuários')
    print('3 - para atualizar um usuário')
    print('4 - para deletar um usuário')
    print('5 - para mostrar um usuário')
    print('-------------------')

    option = input('Digite a opção desejada: ')

    return option

  def user_data(self):
    try:
      id = int(input('Digite o ID do usuário: '))
      name = str(input('Digite o nome do usuário: '))
      email = str(input('Digite o email do usuário: '))
      age = int(input('Digite a idade do usuário: '))

    except:
      self.close_script('Dados inválidos')

    if name == '' or email == '' or age == '' or name == None or email == None or age == None:
      self.close_script('Todos os campos são obrigatórios')

    if '@' not in email:
      self.close_script('Email inválido')

    if age == 0 or age < 0 or age > 80:
      self.close_script('Idade inválida')

    return id, name, email, age

  def create_user(self, name, email, age):
    try:
      self.database.execute("INSERT INTO users (name, email, age) VALUES ('{0}', '{1}', {2})".format(name, email, age))

      self.database.commit()

    except:
      self.close_script('Usuário já cadastrado')

    return None

  def read_users(self):
    user = self.database.execute("SELECT * FROM users")

    if user == None:
      self.close_script('Não há usuários cadastrados')

    return user

  def update_user(self, id, name, email, age):
    try:
      self.database.execute("UPDATE users SET name = '{0}', email = '{1}', age = {2} WHERE id = {3}".format(name, email, age, id))

      self.database.commit()

    except:
      self.close_script('Usuário não atualizado')

    return None

  def delete_user(self):
    try:
      id = int(input('Digite o ID do usuário: '))

      if id == '' or id == None:
        self.close_script('ID inválido')

      self.database.execute("DELETE FROM users WHERE id = {0}".format(id))

      self.database.commit()

    except:
      self.close_script('Usuário não deletado')

    return None

  def show_user(self):
    try:
      id = int(input('Digite o ID do usuário: '))

      if id == '' or id == None:
        self.close_script('ID inválido')

      user = self.database.execute("SELECT * FROM users WHERE id = {0}".format(id))

      if user == None or user == '':
        self.close_script('Usuário não encontrado')

      for user in user:
        print('-------------------')
        print('ID: {0}'.format(user[0]))
        print('Nome: {0}'.format(user[1]))
        print('Email: {0}'.format(user[2]))
        print('Idade: {0}'.format(user[3]))
        print('-------------------')

    except:
      self.close_script('Usuário não mostrado')

    return None

  def execute(self):
    option = self.options()

    if option == '1':
      id, name, email, age = self.user_data()

      self.create_user(name, email, age)

      self.close_script('Usuário criado com sucesso!')

    elif option == '2':
      users = self.read_users()

      for user in users:
        print('-------------------')
        print('ID: {0}'.format(user[0]))
        print('Nome: {0}'.format(user[1]))
        print('Email: {0}'.format(user[2]))
        print('Idade: {0}'.format(user[3]))
        print('-------------------')

      self.close_script('Usuários Listados com sucesso!')

    elif option == '3':
      id, name, email, age = self.user_data()

      self.update_user(id, name, email, age)

      self.close_script('Usuário atualizado com sucesso!')

    elif option == '4':
      self.delete_user()

      self.close_script('Usuário deletado com sucesso!')

    elif option == '5':
      self.show_user()

      self.close_script('Usuário mostrado com sucesso!')

    else:
      self.close_script('Opção inválida')

    return None

Main()
