from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Abre navegador visível
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Acessa página de certificação
    page.goto("https://qualidade.apprbs.com.br/certificacao")

    # Preenche dados obrigatórios
    page.fill("input[name='pessoa.nome']", "Allan Henrique")
    page.fill("input[placeholder='(11) 96123-']", "11 3454-4566")
    page.fill("input[placeholder='email@exemplo.com']", "allan@gmail.com")

    # Tenta avançar no formulário
    page.get_by_role("button", name="Avançar").click()

    # Valida mensagem de erro esperada
    expect(page.get_by_text("É necessário informar a base")).to_be_visible()

    # Fecha navegador
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
