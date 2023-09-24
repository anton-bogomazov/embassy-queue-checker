from Driver import Driver

elements = {
    'order_number': 'ctl00_MainContent_txtID',
    'security_code': 'ctl00_MainContent_txtUniqueID',
    'captcha': 'ctl00_MainContent_txtCode',
    'captcha_id': 'ctl00_MainContent_imgSecNum',
    'send_button': 'ctl00_MainContent_ButtonA',
    'accept_button': 'ctl00_MainContent_ButtonB'
}


def read_orders(path='orders.txt'):
    with open(path, 'r') as file:
        links = [line.strip() for line in file]
    return links


def main():
    driver = Driver()
    for uri in read_orders():
        driver.run(uri)
        driver.fill_field(elements['captcha'], input('> Enter captcha: '))
        driver.click_button(elements["send_button"])
        driver.click_button(elements["accept_button"])
        driver.new_tab()


if __name__ == '__main__':
    main()
