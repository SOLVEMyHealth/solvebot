def sexual_health_consultation():
    return "❤️ Sexual health is an important part of overall wellness. What specific area of sexual health would you like information about? (e.g., STI prevention, contraception, general sexual wellness)"

def process_sexual_health_response(topic):
    if "sti" in topic.lower() or "prevention" in topic.lower():
        return "STI prevention involves practicing safe sex, including using condoms and dental dams. Regular testing is also important. Remember, many STIs can be asymptomatic."
    elif "contraception" in topic.lower():
        return "There are many contraception options available, including hormonal methods (pills, patches, injections), barrier methods (condoms, diaphragms), and long-acting reversible contraceptives (IUDs, implants). It's best to discuss with a healthcare provider to find the best option for you."
    else:
        return "General sexual wellness involves open communication with partners, regular check-ups, maintaining good hygiene, and understanding your own body and desires. If you have specific concerns, it's always best to consult with a healthcare professional."
