from pydub import AudioSegment
import numpy as np
from scipy.signal import resample

def robotic_effect(input_file, output_file):
    # Load the audio file
    audio = AudioSegment.from_file(input_file, format="mp4")

    # Convert audio to numpy array
    samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

    # Apply a robotic effect by modulating the audio with a sine wave
    duration = len(samples) / audio.frame_rate
    time = np.linspace(0, duration, len(samples))
    modulation_frequency = 30  # Frequency of the robotic modulation
    sine_wave = np.sin(2 * np.pi * modulation_frequency * time)
    modulated_samples = samples * sine_wave

    # Normalize the modulated audio
    modulated_samples = np.int16(modulated_samples / np.max(np.abs(modulated_samples)) * 32767)

    # Create a new audio segment with the robotic effect
    robotic_audio = AudioSegment(
        modulated_samples.tobytes(),
        frame_rate=audio.frame_rate,
        sample_width=audio.sample_width,
        channels=audio.channels
    )

    # Export the robotic audio
    robotic_audio.export(output_file, format="mp4", codec="aac")
    print(f"Robotic audio saved to {output_file}")

# Example usage
if __name__ == "__main__":
    input_file = 
    output_file = 
    robotic_effect(input_file, output_file)

