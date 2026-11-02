
import json
from datetime import datetime

from modules.email_analyzer import analyze_email
from modules.dns_intel import get_dns_records


def main():

    print("""
================================
        GHOSTTRACE v1.0
     DIGITAL RECON ENGINE
================================
""")

    name = input("[?] Target name: ").strip()
    email = input("[?] Target email: ").strip()

    print("\n[+] Starting investigation...")

    # Stage 1: Email analysis
    print("\n[01] EMAIL INTELLIGENCE")

    email_results = analyze_email(email)

    print("[+] Email analysis complete.")

    # Stage 2: DNS analysis
    print("\n[02] DOMAIN INTELLIGENCE")

    if email_results.get("valid_format"):

        domain = email.split("@")[1]

        dns_results = get_dns_records(domain)

        print("[+] DNS investigation complete.")

    else:

        dns_results = {
            "error": "Invalid email format"
        }

        print("[-] Invalid email address.")

    # Stage 3: Generate report
    report = {
        "target": name,
        "email_analysis": email_results,
        "domain_intelligence": dns_results,
        "investigation_time": datetime.now().isoformat()
    }

    # Stage 4: Save report
    with open("reports/investigation.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\n================================")
    print("INVESTIGATION COMPLETE")
    print("================================")

    print(json.dumps(report, indent=4))

    print("\n[+] Investigation report saved.")
    print("[+] Location: reports/investigation.json")


if __name__ == "__main__":
    main()
