# Roadmap

## Escolha de framework de sec
Inicialmente eu tava pensando em usar o flask security, porém vou optar por algo mais simples.
Vou criar tudo do zero, tentando me basear no que lembro do flask security.

Segue uma lista de tópicos que preciso implementar:
1. Criação de funcionalidade de encriptação baseada em salt
2. Criação de sistema de roles, com permissões mínimas para cada caso de uso
3. Criação de funcionalidade para autenticação e logout de usuário
4. Criação de funcionalidade para determinar o usuário autenticado naquela requisição
5. Criação de funcionalidade para manipular o cookie de sessão do usuário, visando atualizar as informações da sessão
6. Criação de funcionalidade de expiração de sessão

Lista de melhorias:
1. Integração com email no-reply para gestão de senha;
2. Integração com email para 2-FA
3. Integração com aplicativo de OTP
