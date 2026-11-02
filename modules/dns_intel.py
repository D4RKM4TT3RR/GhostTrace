import dns.resolver

def get_dns_records(domain):

    results = {
        "domain": domain,
        "MX": [],
        "NS": [],
        "TXT": []
    }

    for record_type in ["MX", "NS", "TXT"]:

        try:
            records = dns.resolver.resolve(domain, record_type)

            for record in records:
                results[record_type].append(str(record))

        except Exception:
            results[record_type] = []

    return results
