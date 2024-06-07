# CRUD

# Usuários

userLista = []
opEscolhida = 0

while(opEscolhida != 5):
    opEscolhida = int(input(f'>>>>> MENU <<<<<\n\n1 - Cadastrar User\n2 - Deletar User\n3 - Editar Users\n4 - Listar Users\n5 - Sair\n\nOpção: '))
    
    match opEscolhida:
        case 1:
            addUser = input('User a cadastrar: ')
            userLista.append(addUser)
            print('User Cadastrado! :D')
            
        case 2:
            delUser = input('User a deletar: ')
            
            for user in userLista:
                if delUser == user:         
                    userPos = userLista.index(user)
                    print(userPos)
                    
            userLista.pop(userPos)                    
            print('User Deletado! :/')
            
        case 3:
            
            editUser = input('User a editar: ')
            
            for user in userLista:
                if editUser == user:         
                    userPos = userLista.index(editUser)
                    print(userPos)
                    
            newUser = input('Novo user:')
            userLista[userPos] = newUser                    
            print('User Editado! :D')
            
        case 4:
            print(f'Lista de Users Cadastrados\n\n{userLista}')
            
        case 5:
            print('Tchauuuuuuu!')
            
        case other:
            print('Opção inválida! :(')
