from behave import given, when, then # pylint: disable=no-name-in-module


#Variavel com a URL do site que iremos interagir
base_url = 'https://www.motomaniajundiai.com.br/'

@given(u'acesso a pagina inicial da Moto Mania.')
def step_impl(context):
    context.web.get(base_url)

@when(u'clico no menu Marca.')
def step_impl1(context):
    context = context.web.find_element_by_link_text('Marcas')

@when(u'seleciono a marca Honda.')
def step_impl2(context):
    context = context.web.find_element_by_class_name('topoMarcas')

@then(u'devo visualizar motos da marca honda.')
def step_impl3(context):
    context = context.web.find_element_by_class_name('honda')
    link = context.get_attribute('href')
    print('Link da pagina:' + link)


