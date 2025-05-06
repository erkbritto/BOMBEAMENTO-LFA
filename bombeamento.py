# Programa para demonstrar o Lema de Bombamento em Python
# Objetivo: Provar que a linguagem L = { a^n b^n | n >= 0 } não é regular
# Utilizando o Lema de Bombamento com uma cadeia w e valor de bombamento p

# Função para verificar se uma cadeia pertence à linguagem L
def is_in_L(s):
    """Verifica se a cadeia s pertence à linguagem L = { a^n b^n | n >= 0 }.
       Retorna True se s for da forma 'aaa...a' seguido de 'bbb...b' com igual número de a's e b's,
       False caso contrário."""
    n = len(s)
    if n % 2 != 0:  # Comprimento deve ser par
        return False
    k = n // 2
    # Verifica se a cadeia é k 'a's seguidos de k 'b's
    return s == 'a' * k + 'b' * k

# Função para executar o teste do Lema de Bombamento
def pump_lemma_test(w, p):
    """Simula o Lema de Bombamento para a cadeia w com valor de bombamento p.
       Gera divisões w = xyz, testa repetições de y e analisa os resultados."""
    
    # Cabeçalho inicial estilizado
    print("=" * 60)
    print("🌟 TESTE DO LEMA DE BOMBAMENTO 🌟".center(60))
    print("=" * 60)
    print(f"\n📌 Linguagem analisada: L = {{ a^n b^n | n >= 0 }}")
    print(f"📌 Valor de bombamento (p): {p}")
    print(f"📌 Cadeia escolhida (w): '{w}' (comprimento = {len(w)})")
    print(f"📌 Verificação inicial: w pertence a L? {'Sim ✅' if is_in_L(w) else 'Não ❌'}")
    print("-" * 60)

    # Gerar divisões w = xyz com |xy| <= p e |y| >= 1
    divisions = []
    for m in range(1, p + 1):  # m é o comprimento de xy
        for split_index in range(0, m):  # Ponto de divisão entre x e y
            x = w[0:split_index]
            y = w[split_index:m]
            z = w[m:]
            if y:  # Garante que |y| >= 1
                divisions.append((x, y, z))

    # Exibir divisões
    print("\n🔹 DIVISÕES POSSÍVEIS DE w = xyz (com |xy| <= p e |y| >= 1):")
    print("-" * 60)
    for idx, (x, y, z) in enumerate(divisions, 1):
        print(f"Divisão {idx}:")
        print(f"  x = '{x}' (comprimento: {len(x)})")
        print(f"  y = '{y}' (comprimento: {len(y)})")
        print(f"  z = '{z}' (comprimento: {len(z)})")
        print("-" * 40)

    # Simular repetições de y para i = 0, 1, 2
    print("\n🔹 SIMULAÇÃO DAS REPETIÇÕES DE y (para i = 0, 1, 2):")
    print("-" * 60)
    for idx, (x, y, z) in enumerate(divisions, 1):
        print(f"\nDivisão {idx}: x = '{x}', y = '{y}', z = '{z}'")
        print("Resultados das repetições:")
        print("-" * 40)
        for i in [0, 1, 2]:
            pumped = x + (y * i) + z  # Construir xy^i z
            in_L = is_in_L(pumped)
            status = "✅ Pertence a L" if in_L else "❌ Não pertence a L"
            print(f"  i = {i}: Cadeia resultante = '{pumped}'")
            print(f"       {status} (comprimento: {len(pumped)})")
        print("-" * 40)

    # Conclusão estilizada
    print("\n🔹 CONCLUSÃO FINAL:")
    print("-" * 60)
    print("💡 Para cada divisão w = xyz com |xy| <= p e |y| >= 1:")
    print("   - Existe um valor de i ≠ 1 (como i = 0 ou i = 2) onde xy^i z não pertence a L.")
    print("   - Isso viola o Lema de Bombamento, que afirma que toda linguagem regular")
    print("     deve satisfazer a propriedade de bombamento.")
    print("\n📜 Portanto, a linguagem L = { a^n b^n | n >= 0 } NÃO É REGULAR.")
    print("=" * 60)

# Configuração e execução
if __name__ == "__main__":
    # Definir parâmetros
    p = 3  # Valor de bombamento
    w = "aaabbb"  # Cadeia em L com |w| >= p

    # Executar o teste
    pump_lemma_test(w, p)