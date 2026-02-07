import asyncio
import random
import time
import json
from datetime import datetime
import sys


REQUESTS_PER_DEVICE = 10000

DEVICE_IDS = [              
    'zfCyXhx7fl0YYb2eq1oQmQ==',
    'XewbQ+6LAq2f9gILg+FCtw==',
    'LljJLjnadaQwmLwev2l2fQ==',
    's/QjYd/usbLjg+1/8QZVew==',
    'MoOSSEDJis7GmECPtT4e2g==',
]


async def send_request(device_id: str, rnd: random.Random):
    temperature = rnd.randint(-100, 200)
    humidity = rnd.randint(0, 100)
    signal_strength = rnd.randint(-200, 0)
    power = rnd.randint(0, 100)
    timestamp = datetime.utcnow().isoformat()

    json_body = json.dumps({
        "timestamp": timestamp,
        "temperature": temperature,
        "humidity": humidity,
        "signalStrength": signal_strength,
        "power": power
    })

    process = await asyncio.create_subprocess_exec(
        "curl",
        "-X", "POST",
        "http://localhost:5154/api/DeviceLogs",
        "-H", "accept: */*",
        "-H", f"DeviceId: {device_id}",
        "-H", "Content-Type: application/json",
        "-d", json_body,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE  
    )

    _, stderr = await process.communicate()

    if process.returncode != 0:
        print(f"❌ فشل الإرسال | DeviceId={device_id}", file=sys.stderr)
        print(stderr.decode(), file=sys.stderr)


async def main():
    rnd = random.Random()
    total_requests = len(DEVICE_IDS) * REQUESTS_PER_DEVICE

    # ⏱️ بدء قياس الزمن
    start_time = time.perf_counter()

    tasks = []

    for device_id in DEVICE_IDS:
        for _ in range(REQUESTS_PER_DEVICE):
            tasks.append(send_request(device_id, rnd))

    await asyncio.gather(*tasks)

    # ⏱️ إيقاف التوقيت
    end_time = time.perf_counter()
    duration_ms = (end_time - start_time) * 1000

    print(f"🚀 تم إرسال {total_requests} طلب")
    print(f"⏱️ الزمن الكلي: {int(duration_ms)} ms")
    print(f"⏱️ الزمن بالثواني: {duration_ms / 1000:.2f}")
    print(
        f"📊 متوسط الزمن لكل طلب: "
        f"{duration_ms / total_requests:.2f} ms"
    )


if __name__ == "__main__":
    asyncio.run(main())
