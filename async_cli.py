import sys
import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


async def process_number(number):
    logging.info(f"Feldolgozás indul: {number}")

    await asyncio.sleep(1)

    result = number * 2

    logging.info(f"Eredmény: {result}")

    return result


async def main():
    logging.info("Program indulása")

    numbers = []

    for arg in sys.argv[1:]:
        try:
            number = int(arg)
            numbers.append(number)
            logging.info(f"Beolvasott szám: {number}")

        except ValueError:
            logging.error(f"Hibás paraméter, nem szám: {arg}")

    results = await asyncio.gather(
        *(process_number(num) for num in numbers)
    )

    print("Végeredmények:", results)


if __name__ == "__main__":
    asyncio.run(main())