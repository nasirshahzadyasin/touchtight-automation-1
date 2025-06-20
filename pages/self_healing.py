import logging
from playwright.sync_api import TimeoutError

logging.basicConfig(filename='healing.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def self_healing_locator(page, selectors, context_name="unknown"):
    for selector in selectors:
        try:
            element = page.locator(selector)
            element.wait_for(state="visible", timeout=10000)
            if selector != selectors[0]:
                msg = f"[SELF-HEALING] Used fallback '{selector}' for '{context_name}'"
                logging.info(msg)
                print(msg)
            return element
        except TimeoutError:
            continue
    msg = f"[FAILURE] Could not find visible element '{context_name}' with any selector"
    logging.warning(msg)
    raise TimeoutError(msg)
