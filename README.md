# Exercicios_lista
Peço desculpas pelo erro. Vamos corrigir o código para garantir que ele funcione corretamente para contar as vogais em uma string de 5 caracteres:

```python
while True:
    print("\nMenu:")
    print("1- Tabuada")
    print("2- Vogais")
    print("0- Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '2':
        texto = input("Digite 5 caracteres para contar as vogais: ")
        if len(texto) != 5:
            print("Por favor, digite exatamente 5 caracteres.")
            continue
        
        vogais = 'aeiouAEIOU'
        contador = 0
        for char in texto:
            if char in vogais:
                contador += 1
        print(f"{contador} vogais")
    elif opcao == '0':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")
```

Agora o código verifica se a entrada do usuário tem exatamente 5 caracteres antes de contar as vogais. Se a entrada não tiver o tamanho correto, ele solicitará ao usuário que insira novamente os 5 caracteres.