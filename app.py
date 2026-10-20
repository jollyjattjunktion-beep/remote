import asyncio
from pathlib import Path
import edge_tts

async def main():
    output = Path('output')
    output.mkdir(exist_ok=True)
    target = output / 'preet-sports-test.mp3'
    await edge_tts.Communicate('Welcome to Preet Sports live cricket commentary!', 'en-IN-NeerjaNeural').save(str(target))
    print(f'Created: {target.resolve()}')

if __name__ == '__main__':
    asyncio.run(main())
