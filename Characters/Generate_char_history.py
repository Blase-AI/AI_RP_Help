import openai
import logging
from Characters import Character

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class CharacterHistory(Character):
    def __init__(self, name, race, char_class, openai_api_key):
        super().__init__(name, race, char_class)
        openai.api_key = openai_api_key
        self.history = self.generate_history()

    def generate_history(self, max_tokens=150, temperature=0.7):
        prompt = f"Создай предысторию для персонажа. Он/она — {self.name}, {self.race}, {self.char_class}. Придумай интересную и увлекательную историю, подходящую для такого персонажа."

        try:
            logging.info(f"Запрос на создание истории: {prompt}")

            response = openai.completions.create(
                model="gpt-4",
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature
            )

            logging.info(f"Ответ от OpenAI получен: {response}")

            history = response['choices'][0]['text'].strip()
            return history

        except openai.error.OpenAIError as e:
            logging.error(f"Ошибка при подключении к OpenAI: {e}")
            return "Ошибка при подключении к серверу."

        except Exception as e:
            logging.error(f"Неизвестная ошибка: {e}")
            return "Произошла ошибка при генерации истории."

if __name__ == "__main__":
    openai_api_key = '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'

    if not openai_api_key:
        logging.error("API-ключ OpenAI не задан. Пожалуйста, убедитесь, что ключ указан.")
        exit(1)

    name = "Thalor"
    race = "Elf"
    char_class = "Mage"

    character = CharacterHistory(name, race, char_class, openai_api_key)

    print(f"Character: {character.display_stats()}")
    print(f"History: {character.history}")
