def parse_price(text):
    """Turn a price string like "$1,299.99" into a float (1299.99)."""
    if text is None:
        raise ValueError("price is empty")

    # .replace("CAD", "") removed this function to verify the test fails
    cleaned = text.strip().replace("$", "").replace(",", "").strip()
    if cleaned == "":
        raise ValueError("price is empty")

    try:
        return float(cleaned)
    except ValueError:
        raise ValueError(f"not a price: {text!r}")
