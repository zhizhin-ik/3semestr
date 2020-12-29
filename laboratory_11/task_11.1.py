# Функция gather() модуля asyncio одновременно запускает объекты ожидания. Сначала начнется выполнение для A, но после
# того, как выведется "Task A: Compute factorial(2)...", функция засыпает, и в это время запускается выполнение для B,
# которая также после "Task B: Compute factorial(2)..." засыпает, и так как первая еще спит запустится выполнение для C,
# которая после "Task C: Compute factorial(2)..." заснет. Далее проснется А и выведется "Task A: factorial(2) = 2" и
# закончится ее работа. Проснется B, продолжится выполнение for'а, она заснет, проснется C и так далее

import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()