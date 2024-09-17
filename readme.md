01-LISTAR TODOS USUARIOS
http://127.0.0.1:5000/usuarios


02-CRIAR USUARIO
curl -X POST http://127.0.0.1:5000/usuario -H "Content-Type: application/json" -d "{\"name\": \"Alice Smith\", \"email\": \"alaaaice@example.com\", \"password\": \"securepassword\", \"is_active\": true, \"cpf_cnpj\": \"12345678900\"}"


03-ATUALIZAR USUARIO
curl -X PUT http://127.0.0.1:5000/usuario/1 -H "Content-Type: application/json" -d "{\"name\": \"Alice Smith\", \"email\": \"alice@example.com\", \"password\": \"newpassword\", \"is_active\": false, \"cpf_cnpj\": \"12345678900\"}"


04-BUSCAR USUARIO PELO ID
curl -X GET http://127.0.0.1:5000/usuario/1


05-INATIVAR USUARIO
curl -X PUT http://127.0.0.1:5000/usuario/1/status -H "Content-Type: application/json" -d "{\"is_active\": false}"


06-ATIVAR USUARIO
curl -X PUT http://127.0.0.1:5000/usuario/1/status -H "Content-Type: application/json" -d "{\"is_active\": true}"


07-SALVAR PRODUTO
curl -X POST http://127.0.0.1:5000/produto -H "Content-Type: application/json" -d "{\"nome\": \"Produto1\", \"quantidade\": 10, \"preco\": 19.99}"


08-ATUALIZAR PRODUTO 
curl -X PUT http://127.0.0.1:5000/produto/1 -H "Content-Type: application/json" -d "{\"nome\": \"Produto Atualizado\", \"quantidade\": 20}"


09-LISTAR PRODUTO PELO ID 
curl -X GET http://127.0.0.1:5000/produto/1


10-LISTAR TODOS PRODUTOS
http://127.0.0.1:5000/produto


11-EXCLUIR USUARIO 
curl -X DELETE http://127.0.0.1:5000/usuario/1




