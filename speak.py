# speak.py
import asyncio
import edge_tts
import subprocess
import sys
import os

async def speak_text(text, voice="zh-TW-YunJheNeural"):
    output_mp3 = "temp_speech.mp3"
    
    # 1. 語音合成
    print(f"Generating TTS for: {text[:15]}...")
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_mp3)
    
    # 2. 本機播放 (Windows PresentationCore)
    print("Playing...")
    ps_cmd = f"""
    Add-Type -AssemblyName PresentationCore
    $player = New-Object System.Windows.Media.MediaPlayer
    $player.Open('{os.path.abspath(output_mp3)}')
    Start-Sleep -Seconds 1
    $player.Play()
    Start-Sleep -Seconds 15
    $player.Close()
    """
    subprocess.run(["powershell", "-Command", ps_cmd], capture_output=True)
    
    # 3. 清理
    if os.path.exists(output_mp3):
        os.remove(output_mp3)
    print("Completed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python speak.py 'your text'")
        sys.exit(1)
    asyncio.run(speak_text(sys.argv[1]))
