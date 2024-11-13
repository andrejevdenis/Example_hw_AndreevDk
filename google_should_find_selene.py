from selene import browser, be, have


browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('налог ру').press_enter()
browser.element('[href="https://www.nalog.gov.ru/"]').press_enter()
browser.element('[href="https://lkfl2.nalog.ru/lkfl/login"]').press_enter()
browser.element('[id="username_1"]').type('631108262591')
browser.element('[id="password_2"]').type('*V20242003').press_enter()
browser.element('[data-qa="header-container"]').should(have.text('Личный'))