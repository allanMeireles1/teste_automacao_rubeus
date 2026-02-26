from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Abre navegador
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Acessa página principal
    page.goto("https://qualidade.apprbs.com.br/site")

    # Valida que link Atendimento abre nova aba
    with page.expect_popup() as atendimento_popup:
        page.get_by_role("link", name="Atendimento").click()
    atendimento_popup.value.close()

    # Valida que link WhatsApp abre nova aba
    with page.expect_popup() as whatsapp_popup:
        page.get_by_role("link", name="WhatsApp").click()
    whatsapp_popup.value.close()

    # Preenche formulário principal
    page.fill("input[name='pessoa.nome']", "Allan Henrique")
    page.fill("input[placeholder='email@exemplo.com']", "emailteste@exemplo.com")
    page.fill("input[placeholder='(11) 96123-']", "82 4536-7642")

    # Envia formulário
    page.get_by_role("button", name="Concluir").click()

    # (Opcional) validar mensagem de sucesso se existir
    # expect(page.get_by_text("Mensagem enviada")).to_be_visible()

    # Fecha navegador
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
