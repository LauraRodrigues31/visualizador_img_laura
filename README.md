# Bem vindos ao meu visualizador de Imagens com OpenCV e Streamlit

Este projeto é um visualizador interativo de imagens que permite aplicar filtros e transformações diretamente pelo navegador, utilizando a biblioteca **Streamlit** para a interface e **OpenCV** para o processamento de imagem.

## Funcionalidades

- Carregamento de imagens (`.jpg`, `.png`, `.bmp`)
- Aplicação de **filtros**:
  - Escala de Cinza
  - Inversão de Cores
  - Aumento de Contraste
  - Desfoque (Blur)
  - Nitidez (Sharpen)
  - Detecção de Bordas
- Aplicação de **transformações**:
  - Rotações (90°, 180°, 270°)
  - Espelhamento (horizontal e vertical)
  - Redimensionamento com fator de escala
- Download da imagem resultante após as edições

* No final da utilização deste visualizador de imagens será possível fazer memes iguais a esses: 
![Interface do aplicativo](assets/meme-invertido-1.jpg)

* De nada! 

Continuando...
---

## 🧱 Tecnologias e Bibliotecas Utilizadas

| Tecnologia  | Finalidade                               |
|-------------|-------------------------------------------|
| `Streamlit` | Criação da interface web interativa       |
| `OpenCV`    | Processamento e transformação de imagens  |
| `NumPy`     | Manipulação de arrays e matrizes          |
| `Pillow`    | Conversão entre formatos de imagem        |

---

## Arquivos

* app.py # Interface principal em Streamlit

* iltros.py # Funções de filtros (OpenCV)

* transformacoes.py # Funções de transformações (rotação, espelhamento, etc.)

* tils.py # Funções utilitárias (download da imagem)

* requirements.txt # Dependências do projeto


---

#  Como Executar o Projeto

### 1. Clone ou baixe o repositório
```bash
git clone https://github.com/LauraRodrigues31/visualizador_img_laura.git

cd visualizador_img_laura

```
### 2.Crie um ambiente virtual (opcional, mas recomendado)
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

```
## 3. Execute o projeto
```bash
streamlit run app.py

```