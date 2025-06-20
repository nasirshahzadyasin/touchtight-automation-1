from playwright.sync_api import sync_playwright
import re


def format_name(value):
    value = value or "unknown"
    return re.sub(r'\W+', '_', value.strip().lower())


def get_label_for(page, el):
    id_attr = el.get_attribute("id")
    if id_attr:
        label_el = page.query_selector(f"label[for='{id_attr}']")
        if label_el:
            return label_el.inner_text().strip()
    aria = el.get_attribute("aria-label")
    if aria:
        return aria
    return el.inner_text().strip()


def is_valid_selector(value):
    return value and not re.match(r'^#«.*»$', value)


def extract_readable_selectors(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")

        elements = page.query_selector_all("input, button, select, textarea, a")
        printed_keys = set()

        for el in elements:
            if not el.is_visible():
                continue

            tag = el.evaluate("e => e.tagName.toLowerCase()")
            id_attr = el.get_attribute("id")
            name_attr = el.get_attribute("name")
            type_attr = el.get_attribute("type")
            placeholder = el.get_attribute("placeholder")
            text = el.inner_text().strip()
            label = get_label_for(page, el)

            base_name = name_attr or placeholder or label or id_attr or type_attr or text or "unknown"
            key = f"{tag}_{format_name(base_name)}"
            if key in printed_keys:
                counter = 2
                while f"{key}_{counter}" in printed_keys:
                    counter += 1
                key = f"{key}_{counter}"

            printed_keys.add(key)

            selectors = []

            if name_attr:
                selectors.append(f"//{tag}[@name='{name_attr}']")
            if id_attr and is_valid_selector(id_attr):
                selectors.append(f"#{id_attr}")
            if type_attr:
                selectors.append(f"{tag}[type='{type_attr}']")
            if placeholder:
                selectors.append(f"{tag}[placeholder='{placeholder}']")
            if text and tag in ['button', 'a']:
                selectors.append(f"{tag}:has-text('{text}')")

            # remove duplicates and print
            if selectors:
                unique = list(dict.fromkeys(selectors))
                print(f"{key} = {unique}")

        browser.close()


if __name__ == "__main__":
    extract_readable_selectors("https://fe.stag.touchtight.com/login")
