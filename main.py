# This script demonstrates a very basic rule-based AI assistant.
# It simulates understanding user input and providing relevant responses
# about Artificial Intelligence concepts, illustrating a fundamental
# principle of AI: making decisions based on input patterns.

def ai_assistant(user_input):
    """
    Processes user input and returns a predefined response based on keywords.
    This simulates a simple form of 'intelligence' through pattern matching.
    """
    user_input = user_input.lower()

    # Rule-based decision making: The core 'intelligence' here is simple keyword matching.
    # This is a foundational concept, as more advanced AI uses machine learning for complex pattern recognition.
    if "yapay zeka nedir" in user_input or "ai nedir" in user_input or "what is ai" in user_input:
        return "Yapay zeka (YZ), makinelerin insan benzeri zeka sergilemesini sağlayan bir teknoloji alanıdır. Öğrenme, problem çözme, algılama ve karar verme gibi yetenekleri içerir."
    elif "nasıl çalışır" in user_input or "how does it work" in user_input:
        return "YZ genellikle algoritmalar ve büyük veri kümeleri kullanarak öğrenir. Bu algoritmalar, desenleri tanır ve bu bilgilere dayanarak tahminler veya kararlar verir."
    elif "örnekler" in user_input or "uygulamalar" in user_input or "examples" in user_input:
        return "Günlük hayatta YZ'ye örnekler: sesli asistanlar (Siri, Google Assistant), kişiselleştirilmiş öneri sistemleri (Netflix, Spotify), otonom araçlar ve sağlık teşhis sistemleri."
    elif "gelecek" in user_input or "future" in user_input:
        return "Yapay zeka, sağlık, eğitim, ulaşım ve enerji gibi birçok alanda büyük dönüşümler vadediyor. Daha akıllı şehirler, kişiselleştirilmiş tıp ve verimli üretim gibi yenilikler bekleniyor."
    elif "teşekkürler" in user_input or "sağ ol" in user_input or "thank you" in user_input:
        return "Rica ederim! Başka sorun olursa çekinme."
    elif "merhaba" in user_input or "hi" in user_input:
        return "Merhaba! Yapay zeka hakkında ne öğrenmek istersin?"
    else:
        return "Üzgünüm, bu konuda henüz bilgiye sahip değilim. 'Yapay zeka nedir', 'nasıl çalışır' veya 'örnekler' gibi sorular sorabilirsin."

def main():
    print("Merhaba! Ben basit bir Yapay Zeka asistanıyım.")
    print("Yapay zeka hakkında sorularını yanıtlayabilirim.")
    print("Çıkmak için 'çıkış' yazabilirsin.")

    while True:
        user_input = input("\nSen: ")
        if user_input.lower() == "çıkış":
            print("Güle güle!")
            break
        response = ai_assistant(user_input)
        print(f"Asistan: {response}")

if __name__ == "__main__":
    main()
