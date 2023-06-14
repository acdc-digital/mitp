import re

def apply_privacy_filter(text, privacy_data):
    """
    This function applies a privacy filter to the given text, replacing sensitive information
    with asterisks based on the provided privacy_data.

    :param text: str, the text to apply the privacy filter to
    :param privacy_data: list, a list of sensitive information to be replaced
    :return: str, the text with sensitive information replaced by asterisks
    """
    for data in privacy_data:
        pattern = re.compile(re.escape(data), re.IGNORECASE)
        text = pattern.sub('*' * len(data), text)
    return text