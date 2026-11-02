import re
import dns.resolver

def analyze_email(email):

    result = {
        "email": email,
        "valid_format": False,
        "domain": None,
        "mx_records": []
    }

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    if not re.match(pattern, email):
        return result

    result["valid_format"] = True

    domain = email.split("@")[1]
    result["domain"] = domain

    try:
        records = dns.resolver.resolve(domain, "MX")

        for record in records:
            result["mx_records"].append(str(record.exchange))

    except Exception:
        pass

    return result
