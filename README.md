## Bot criado em Python, para realizar visualizações nos videos mais recentes do meus canais favoritos.

* *Determino duas variaveis, uma vai conter uma lista com os ID doa canais e a outra vai conter o url padrão dos canais do youtube*

1. **Variavel dos ID dos canais**
```python
channels = [
    'UC8butISFwT-Wl7EV0hUK0BQ',
    'UCh9nVJoWXmFb7sLApWGcLPQ',
    'UC4JX40jDee_tINbkjycV4Sg'
]
```
2. **Váriavel com a URL padrão dos canais no youtube**
```python
url_youtube = 'https://www.youtube.com/channel/'
```
___
___
* *Utilizo o webdriver_manager para instanciar o google chrome e acessar o canal com o método GET, deve ser utilizado um laço de repetição para que seja interado todos os ID de canais da lista, no meu caso eu utilizei o for, pode ser observado dentro do p´roprio código*
```python
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(f'{url_youtube}{channel}')
```
___

* *Com a lib Selenium simulo um click no video mais recente do canal*

```python
from selenium import webdriver

driver.find_element_by_xpath( '//div[contains(@class, "style-scope ytd-grid-video-renderer")]').click()
```
___
___
___
## Nota do Dev
**O Bot foi criado com única e exclusiva finalidade de expandir meus conhecimentos no Python, especificamente no mundo de Web Scraping.**
**Não recomendo o uso desse algoritimo para realizar praticas ílegais dentro da plataforma do youtube**