# 🎬 Manim Tutorial

Repositório dedicado ao aprendizado do **Manim Community Edition (ManimCE)**, biblioteca Python para criação de animações matemáticas e educacionais de forma programática.

O objetivo deste projeto é documentar minha evolução no Manim, reunindo exemplos, experimentos e animações que poderão ser reutilizados em aulas, vídeos e projetos educacionais.

## Objetivos

* Aprender os fundamentos do Manim.
* Criar animações para Matemática e Programação.
* Produzir material didático para alunos do Ensino Médio.
* Explorar recursos avançados como gráficos, LaTeX, animações 3D e câmeras.
* Construir uma biblioteca pessoal de exemplos reutilizáveis.

## Tecnologias

* Python 3
* Manim Community Edition
* LaTeX
* FFmpeg
* VS Code

## Estrutura do projeto

```text
manim_tutorial/
│
├── scenes/          # Exemplos e exercícios
├── assets/          # Imagens, SVGs e outros recursos
├── media/           # Arquivos gerados (ignorado pelo Git)
├── .venv/           # Ambiente virtual (ignorado)
├── requirements.txt
└── README.md
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/manim_tutorial.git
cd manim_tutorial
```

Crie um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Ou apenas:

```bash
pip install manim
```

A documentação oficial recomenda instalar o Manim em um ambiente virtual isolado.

## Executando uma animação

```bash
manim -pqh scenes/introducao.py MinhaCena
```

Parâmetros úteis:

| Opção | Descrição                             |
| ----- | ------------------------------------- |
| `-p`  | Abre o vídeo ao finalizar             |
| `-ql` | Baixa qualidade (renderização rápida) |
| `-qm` | Qualidade média                       |
| `-qh` | Alta qualidade                        |
| `-qk` | Qualidade 4K                          |

## Roadmap

* [ ] Primeira cena
* [ ] Formas geométricas
* [ ] Texto e LaTeX
* [ ] Posicionamento de objetos
* [ ] Transformações
* [ ] Gráficos de funções
* [ ] Sistemas de coordenadas
* [ ] Animações com `ValueTracker`
* [ ] Updaters
* [ ] Câmera
* [ ] Cenas 3D
* [ ] Projetos para aulas de Matemática

## Referências

* Documentação oficial do Manim Community
* Quickstart do Manim
* Galeria oficial de exemplos
* Repositório oficial no GitHub

## Licença

Este projeto é destinado a estudos e uso educacional.
