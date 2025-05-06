# Projeto: Demonstração do Lema de Bombamento

## Descrição
Este repositório contém um programa em Python que ilustra a aplicação do Lema de Bombamento para provar que a linguagem \( L = \{ a^n b^n \mid n \geq 0 \} \) não é regular. O Lema de Bombamento é uma ferramenta fundamental em Linguagens Formais e Autômatos, utilizada para verificar se uma linguagem pode ser reconhecida por um autômato finito.

O programa analisa a cadeia \( w = "aaabbb" \) com um comprimento de bombamento \( p = 3 \), gerando todas as possíveis decomposições \( w = xyz \). Em seguida, verifica se as repetições da forma \( xy^i z \) (para diferentes valores de \( i \)) violam a propriedade de regularidade, confirmando que a linguagem não é regular.

## Integrantes
- **Nome**: Erick de Britto Carvalho  
  **RA**: G78HED3  
- **Nome**: Aluísio Pereira Alves  
  **RA**: N135891  
- **Período**: Noturno  
- **Disciplina**: Linguagens Formais e Autômatos  
