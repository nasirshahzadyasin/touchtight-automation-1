# Signup locators
getStarted_selectors = ["#mui-5", "button:has-text('Get Started')"]
email_input_selectors = ['//input[@name="email"]', 'input[type="email"]']
getStarted_btn_selectors = ['//button[@tabindex="0"]', "button:has-text('Next')"]
fullname_input_selectors = ['//input[@name="fullName"]', 'input[placeholder="Full Name"]']
pwd_input_selectors = ['//input[@name="password"]', 'input[type="password"]']
appsecret_input_selectors = ['//input[@name="appSecret"]']
club_input_selectors = ['//input[@name="clubName"]']
create_acc_btn_selectors = ["//button[text()='Continue']", "button:has-text('Continue')"]
success_message_selectors = ["//*[text()=\"Welcome aboard! We're excited to have you with us.\"]"]

# login locators
login_link_xpath = ["//p[text()='Login']"]
login_email_input_selectors = ['//input[@name="email"]', 'input[type="email"]']
password_input_selectors = ['//input[@name="password"]', 'input[type="password"]']
button_log_in = ['//button[contains(text(), "log in")]']
verify_login_success = ["//*[text()='Most Popular']", "//*[text()='My Library']"]

# logout locators
profile_icon_xpath = ["//div[@class='MuiGrid-root MuiGrid-direction-xs-row css-1n5khr6']/div[@class='MuiGrid-root MuiGrid-container MuiGrid-direction-xs-row css-810z3n']"]
logout_btn_xpath = ['//*[contains(text(), "Log Out")]']
home_text_path = ['//*[contains(text(), "Most Popular")]']
