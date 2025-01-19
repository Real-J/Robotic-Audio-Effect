# Robotic Audio Effect

This repository contains a Python script to apply a robotic effect to audio files using the `pydub` and `numpy` libraries. The effect is achieved by modulating the audio signal with a sine wave.

## Features
- Applies a robotic modulation effect to audio files.
- Supports `.mp4` audio input and output.
- Utilizes `pydub` for audio processing and `numpy` for numerical computations.

## Requirements

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- `pydub`
- `numpy`
- `scipy`
- `ffmpeg` or `libav` (required by `pydub` for handling `.mp4` files)

Install the required Python packages using pip:

```bash
pip install pydub numpy scipy
```

Make sure `ffmpeg` or `libav` is installed on your system. For example, on Ubuntu:

```bash
sudo apt update
sudo apt install ffmpeg
```

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/robotic-audio-effect.git
   cd robotic-audio-effect
   ```

2. Place your input audio file (in `.mp4` format) in the same directory as the script.

3. Run the script with the following command:

   ```bash
   python robotic_effect.py
   ```

4. Specify the input and output file paths in the script or modify the following lines to point to your desired files:

   ```python
   input_file = "your_audio_file.mp4"
   output_file = "robotic_audio.mp4"
   ```

5. The output audio file with the robotic effect will be saved in the specified location.

## Example

Input: `input_audio.mp4`  
Output: `robotic_audio.mp4`

## How It Works

The script applies a robotic effect by:
1. Loading the input audio file using `pydub`.
2. Converting the audio samples to a NumPy array.
3. Modulating the audio signal with a sine wave of a specified frequency.
4. Normalizing the audio to ensure the output is within a valid range.
5. Exporting the processed audio as an `.mp4` file.

## Customization

- **Modulation Frequency**: Adjust the `modulation_frequency` parameter to control the robotic effect's intensity:
  ```python
  modulation_frequency = 30  # Frequency in Hz
  ```

- **Input/Output Format**: Modify the `input_file` and `output_file` variables to handle other file formats supported by `pydub`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository, create a branch, and submit a pull request if you have ideas for improvements or new features.

## Author

Developed by [Your Name](https://github.com/yourusername).

## Acknowledgments

- [pydub documentation](https://pydub.com/)
- [numpy documentation](https://numpy.org/)
- [ffmpeg documentation](https://ffmpeg.org/)

