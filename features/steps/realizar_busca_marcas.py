from behave import given, when, then # pylint: disable=no-name-in-module
from selenium.webdriver.common.keys import Keys

#Variavel com a URL do site que iremos interagir
base_url = 'https://www.motomaniajundiai.com.br/'

@when(u'clico na busca.')
def step_impl(context):
    context.web.get(base_url)


@when(u'informo o termo Honda.')
def step_impl1(context):

    # pegar o campo de busca onde podemos digitar algum termo
    campo_busca = context.web.find_element_by_class_name('btnActiveProcura')

    # Digitar "Python Club" no campo de busca
    campo_busca.send_keys('Honda')

    # Simular que o enter seja precisonado
    campo_busca.send_keys(Keys.ENTER)